from celery import shared_task
from DownloadExcel import downloadexcel_codes as dc
import os
from django.conf import settings
import shutil
import uuid
import time

@shared_task
def generate_excel_file(export_type, object_id, xml_list, excel_format='simple'):
    unique_suffix = uuid.uuid4().hex
    if excel_format == 'asphaltmine':
        final_path = dc.main(xml_list, unique_suffix)
        prefix = "AsphaltMine"
        extension = "xlsx"
    elif excel_format == 'csv':
        final_path = dc.main_csv(xml_list, unique_suffix)
        prefix = "AsphaltMine_SimpleExport"
        extension = "csv"
    else:
        final_path = dc.main_simple(xml_list, unique_suffix)
        prefix = "AsphaltMine_SimpleExport"
        extension = "xlsx"
    if export_type == 'user':
        filename = f"{prefix}_My_Data_{object_id}{unique_suffix}.{extension}"
    elif export_type == 'workspace':
        filename = f"{prefix}_Workspace_Data_{object_id}{unique_suffix}.{extension}"
    elif export_type == 'query':
        filename = f"{prefix}_All_Viewable_Data_{object_id}{unique_suffix}.{extension}"
    elif export_type == 'selected':
        filename = f"{prefix}_Selected_Data_{unique_suffix}.{extension}"
    os.makedirs(settings.MEDIA_ROOT, exist_ok=True)
    excel_file_path = os.path.join(settings.MEDIA_ROOT, filename)
    shutil.move(final_path, excel_file_path)

    initial_path = os.path.join(settings.BASE_DIR, f"Initial_Download_{unique_suffix}.xlsx")
    if os.path.exists(initial_path):
        os.remove(initial_path)

    return filename

@shared_task
def cleanup_media(max_age_hours=1):
    now = time.time()
    max_age_seconds = max_age_hours * 3600
    for dirname, _, filenames in os.walk(settings.MEDIA_ROOT):
        for filename in filenames:
            filepath = os.path.join(dirname, filename)
            if os.path.isfile(filepath):
                file_age = now - os.path.getmtime(filepath)
                if file_age > max_age_seconds:
                    os.remove(filepath)

@shared_task
def refresh_live_insights_overview():
    from Visualization import live_insights_service as li
    li.refresh_all_parsed_records_cache()
