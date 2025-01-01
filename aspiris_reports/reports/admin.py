from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin, ImportMixin
from .models import SalesData

from import_export import resources
from .models import SalesData
from import_export.admin import ImportExportModelAdmin


@admin.register(SalesData)


class ViewAdmin(ImportExportModelAdmin):
    pass

# class SalesDataResource(resources.ModelResource):
#     class Meta:
#         model = SalesData
       
#     def before_import_row(self, row, **kwargs):
#         # Ensure 'id' is not present in the row data
#         if 'id' in row:
#             del row['id']
#         return row

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportMixin
from .models import SalesTarget

class SalesTargetResource(resources.ModelResource):
    class Meta:
        model = SalesTarget

class SalesTargetAdmin(ImportMixin, admin.ModelAdmin):
    resource_class = SalesTargetResource

admin.site.register(SalesTarget, SalesTargetAdmin)

