from django.test import TestCase, Client
from .models import CustomUser, Project, Experience, Skill, Connection
from django.core.exceptions import ValidationError
from django.urls import reverse
from .forms import ConnectionForm
from django.contrib.auth import get_user_model

class CustomUserManagerTestCase(TestCase):
    def setUp(self):
        self.user_manager = CustomUser.objects
        self.user_data = {
            'email': 'test@example.com',
            'first_name': 'Marshal',
            'last_name': 'Kallou',
            'phone_number': '0782309009',
            'home_address': '7561 Old Highfield',
        }

    def test_create_user(self):
        user = self.user_manager.create_user(**self.user_data, password='password')
        self.assertEqual(user.email, self.user_data['email'])
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_user_no_email(self):
        with self.assertRaises(ValueError):
            self.user_manager.create_user(email='', password='password')

    def test_create_superuser(self):
        superuser = self.user_manager.create_superuser(**self.user_data, password='password')
        self.assertEqual(superuser.email, self.user_data['email'])
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

class ProjectTestCase(TestCase):
    def setUp(self):
        self.project_data = {
            'title': 'My Project',
            'description': 'This is a description of my project',
            'github_link': 'https://github.com/Kallou0/myproject',
            'tech_stack': 'Django, React',
        }

    def test_create_project(self):
        project = Project.objects.create(**self.project_data)
        self.assertEqual(project.title, self.project_data['title'])
        self.assertEqual(project.description, self.project_data['description'])
        self.assertEqual(project.github_link, self.project_data['github_link'])
        self.assertEqual(project.tech_stack, self.project_data['tech_stack'])

    def test_get_project_by_title(self):
        project = Project.objects.create(**self.project_data)
        retrieved_project = Project.objects.get(title=self.project_data['title'])
        self.assertEqual(project, retrieved_project)

    def test_update_project(self):
        project = Project.objects.create(**self.project_data)
        new_title = 'New Title'
        project.title = new_title
        project.save()
        updated_project = Project.objects.get(id=project.id)
        self.assertEqual(updated_project.title, new_title)

class ExperienceTestCase(TestCase):
    def setUp(self):
        self.experience_data = {
            'designation': 'Software Developer',
            'start_date': '2022-01-01',
            'end_date': '2022-12-31',
            'is_present': False,
            'responsibilities_1': 'Developed web applications',
            'responsibilities_2': 'Implemented new features',
            'responsibilities_3': 'Testing',
            'responsibilities_4': 'Deployment',
            'company': 'Zimswitch',
            'location': 'Harare, Zimbabwe',
        }

    def test_create_experience(self):
        experience = Experience.objects.create(**self.experience_data)
        self.assertEqual(experience.designation, self.experience_data['designation'])
        self.assertEqual(str(experience.start_date), self.experience_data['start_date'])
        self.assertEqual(str(experience.end_date), self.experience_data['end_date'])
        self.assertEqual(experience.is_present, self.experience_data['is_present'])
        self.assertEqual(experience.responsibilities_1, self.experience_data['responsibilities_1'])
        self.assertEqual(experience.company, self.experience_data['company'])
        self.assertEqual(experience.location, self.experience_data['location'])

    def test_get_experience_by_designation(self):
        experience = Experience.objects.create(**self.experience_data)
        retrieved_experience = Experience.objects.get(designation=self.experience_data['designation'])
        self.assertEqual(experience, retrieved_experience)

    def test_update_experience(self):
        experience = Experience.objects.create(**self.experience_data)
        new_designation = 'Senior Software Developer'
        experience.designation = new_designation
        experience.save()
        updated_experience = Experience.objects.get(id=experience.id)
        self.assertEqual(updated_experience.designation, new_designation)

    def test_delete_experience(self):
        experience = Experience.objects.create(**self.experience_data)
        experience.delete()
        with self.assertRaises(Experience.DoesNotExist):
            Experience.objects.get(id=experience.id)

class SkillTestCase(TestCase):
    def setUp(self):
        self.skill_data = {
            'name': 'Python',
            'image': 'https://example.com/python.png',
        }

    def test_create_skill(self):
        skill = Skill.objects.create(**self.skill_data)
        self.assertEqual(skill.name, self.skill_data['name'])
        self.assertEqual(skill.image, self.skill_data['image'])

    def test_get_skill_by_name(self):
        skill = Skill.objects.create(**self.skill_data)
        retrieved_skill = Skill.objects.get(name=self.skill_data['name'])
        self.assertEqual(skill, retrieved_skill)

    def test_update_skill(self):
        skill = Skill.objects.create(**self.skill_data)
        new_name = 'Java'
        skill.name = new_name
        skill.save()
        updated_skill = Skill.objects.get(id=skill.id)
        self.assertEqual(updated_skill.name, new_name)

    def test_delete_skill(self):
        skill = Skill.objects.create(**self.skill_data)
        skill.delete()
        with self.assertRaises(Skill.DoesNotExist):
            Skill.objects.get(id=skill.id)

class ConnectionModelTest(TestCase):
    def test_connection_create(self):
        connection = Connection.objects.create(
            name='Marshy Kallou',
            email='marshal.kallou@gmail.com',
            subject='Test Subject',
            message='Test Message'
        )
        self.assertEqual(str(connection), 'Marshy Kallou')

    
    def test_connection_subject_max_length(self):
        max_length = Connection._meta.get_field('subject').max_length
        connection = Connection.objects.create(
            name='Marshy Kallou',
            email='marshal.kallou@gmail.com',
            subject='X' * max_length,
            message='Test Message'
        )
        self.assertEqual(str(connection), 'Marshy Kallou')



class HomeViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('home')
        self.project = Project.objects.create(title='Test Project', description='Test Description')
        self.skill = Skill.objects.create(name='Test Skill')
        self.experience = Experience.objects.create(
            company='Test Company', designation='Test Position', start_date='2022-01-01', end_date='2022-02-01', responsibilities_1='Test Description',
            responsibilities_2='Test Description',responsibilities_3='Test Description',responsibilities_4='Test Description', location='Harare'
        )
        self.profile = CustomUser.objects.create(
            email='testuser@example.com', first_name='Test', last_name='User', username='testuser', password='testpass', phone_number='1234567890', home_address='Test Address'
        )

    def test_home_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

        projects = response.context['projects']
        self.assertEqual(list(projects), [self.project])

        skills = response.context['skills']
        self.assertEqual(list(skills), [self.skill])

        experiences = response.context['experiences']
        self.assertEqual(list(experiences), [self.experience])

        profile = response.context['profile']
        self.assertEqual(profile, self.profile)

        form = response.context['form']
        self.assertIsInstance(form, ConnectionForm)

class ProfileViewsTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            email='test@example.com',
            password='testpass',
            first_name='Test',
            last_name='User',
            phone_number='0782309009',
            home_address='7561 Old Highfield'
        )

    def test_profile_view(self):
        self.client.login(email='test@example.com', password='testpass')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test')

    def test_edit_profile_view(self):
        self.client.login(email='test@example.com', password='testpass')
        response = self.client.get(reverse('edit_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Edit Profile')