from django.conf.urls import url

from DynamicAnalyzer.views.android import dynamic

from MobSF import utils
from MobSF.views import home
from MobSF.views.api import rest_api

from StaticAnalyzer import tests
from StaticAnalyzer.views import shared_func, windows
from StaticAnalyzer.views.android import find, java, manifest_view, smali
from StaticAnalyzer.views.android import static_analyzer as android_sa
from StaticAnalyzer.views.android import view_source
from StaticAnalyzer.views.ios import static_analyzer as ios_sa
from StaticAnalyzer.views.ios import view_source as io_view_source

urlpatterns = [
    # Examples:
    url(r'^mobsf/$', home.index, name='home'),
    url(r'^mobsf/upload/$', home.Upload.as_view),
    url(r'^mobsf/download/', home.download),
    url(r'^mobsf/about$', home.about, name='about'),
    url(r'^mobsf/api_docs$', home.api_docs, name='api_docs'),
    url(r'^mobsf/recent_scans/$', home.recent_scans, name='recent'),
    url(r'^mobsf/delete_scan/$', home.delete_scan),
    url(r'^mobsf/search$', home.search),
    url(r'^mobsf/error/$', home.error, name='error'),
    url(r'^mobsf/not_found/$', home.not_found),
    url(r'^mobsf/zip_format/$', home.zip_format),
    url(r'^mobsf/mac_only/$', home.mac_only),

    # Static Analysis
    # Android
    url(r'^mobsf/StaticAnalyzer/$', android_sa.static_analyzer),
    url(r'^mobsf/ViewSource/$', view_source.run),
    url(r'^mobsf/Smali/$', smali.run),
    url(r'^mobsf/Java/$', java.run),
    url(r'^mobsf/Find/$', find.run),
    url(r'^mobsf/ManifestView/$', manifest_view.run),
    # IOS
    url(r'^mobsf/StaticAnalyzer_iOS/$', ios_sa.static_analyzer_ios),
    url(r'^mobsf/ViewFile/$', io_view_source.run),
    # Windows
    url(r'^mobsf/StaticAnalyzer_Windows/$', windows.staticanalyzer_windows),
    # Shared
    url(r'^mobsf/PDF/$', shared_func.pdf),
    # We validate the hash sanity in the URL already
    url(r'^mobsf/compare/(?P<hash1>[0-9a-f]{32})/(?P<hash2>[0-9a-f]{32})/$',
        shared_func.compare_apps),

    # Android Dynamic Analysis
    url(r'^mobsf/DynamicAnalyzer/$', dynamic.android_dynamic_analyzer),
    url(r'^mobsf/GetEnv/$', dynamic.get_env),
    url(r'^mobsf/GetRes/$', dynamic.get_res),
    url(r'^mobsf/MobSFCA/$', dynamic.mobsf_ca),
    url(r'^mobsf/TakeScreenShot/$', dynamic.take_screenshot),
    url(r'^mobsf/ClipDump/$', dynamic.clip_dump),
    url(r'^mobsf/ExportedActivityTester/$', dynamic.exported_activity_tester),
    url(r'^mobsf/ActivityTester/$', dynamic.activity_tester),
    url(r'^mobsf/FinalTest/$', dynamic.final_test),
    url(r'^mobsf/DumpData/$', dynamic.dump_data),
    url(r'^mobsf/ExecuteADB/$', dynamic.execute_adb),
    url(r'^mobsf/Report/$', dynamic.report),
    url(r'^mobsf/View/$', dynamic.view),
    url(r'^mobsf/ScreenCast/$', dynamic.screen_cast),
    url(r'^mobsf/Touch/$', dynamic.touch),
    url(r'^mobsf/capfuzz$', dynamic.capfuzz_start),

    # REST API
    url(r'^mobsf/api/v1/upload$', rest_api.api_upload),
    url(r'^mobsf/api/v1/scan$', rest_api.api_scan),
    url(r'^mobsf/api/v1/delete_scan$', rest_api.api_delete_scan),
    url(r'^mobsf/api/v1/download_pdf$', rest_api.api_pdf_report),
    url(r'^mobsf/api/v1/report_json$', rest_api.api_json_report),
    url(r'^mobsf/api/v1/view_source$', rest_api.api_view_source),
    url(r'^mobsf/api/v1/scans$', rest_api.api_recent_scans),

    # Test
    url(r'^mobsf/tests/$', tests.start_test),

]

utils.print_version()
