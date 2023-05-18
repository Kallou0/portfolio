from django.contrib.gis.admin.widgets import OpenLayersWidget

class CustomOpenLayersWidget(OpenLayersWidget):
    template_name = 'gis/openlayers.html'

    def build_attrs(self, base_attrs, extra_attrs=None):
        attrs = super().build_attrs(base_attrs, extra_attrs=extra_attrs)
        if 'name' in attrs:
            attrs.pop('name')
        return attrs

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        if 'name' in context['widget']['attrs']:
            del context['widget']['attrs']['name']
        return context

    def get_js_params(self, value, srid):
        """
        Returns a dictionary of JavaScript parameters to be used during
        the rendering of the widget.
        """
        js_params = {
            'default_lon': float(self.map_settings.get('default_lon', 0.0)),
            'default_lat': float(self.map_settings.get('default_lat', 0.0)),
            'default_zoom': int(self.map_settings.get('default_zoom', 4)),
            'display_wkt': bool(self.map_settings.get('display_wkt', False)),
            'geom_type': self.geom_type,
            'is_collection': self.is_collection,
            'is_linestring': self.is_linestring,
            'is_multipolygon': self.is_multipolygon,
            'is_point': self.is_point,
            'is_polygon': self.is_polygon,
            'max_zoom': int(self.max_zoom),
            'min_zoom': int(self.min_zoom),
            'mouse_position': self.mouse_position,
            'point_zoom': int(self.point_zoom),
            'srid': int(srid),
            'wkt': value,
        }
        return js_params