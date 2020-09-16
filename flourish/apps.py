from datetime import datetime
from dateutil.tz import gettz
from django.apps import AppConfig as DjangoAppConfig

from edc_appointment.apps import AppConfig as BaseEdcAppointmentAppConfig
from edc_appointment.appointment_config import AppointmentConfig
from edc_appointment.constants import COMPLETE_APPT
from edc_base.apps import AppConfig as BaseEdcBaseAppConfig
from edc_data_manager.apps import AppConfig as BaseEdcDataManagerAppConfig
from edc_protocol.apps import AppConfig as BaseEdcProtocolAppConfig
from edc_timepoint.apps import AppConfig as BaseEdcTimepointAppConfig
from edc_timepoint.timepoint import Timepoint
from edc_timepoint.timepoint_collection import TimepointCollection


class AppConfig(DjangoAppConfig):
    name = 'flourish'


class EdcAppointmentAppConfig(BaseEdcAppointmentAppConfig):
    configurations = [
        AppointmentConfig(
            model='edc_appointment.appointment',
            related_visit_model='flourish_maternal.maternalvisit',
            appt_type='clinic')]


class EdcBaseAppConfig(BaseEdcBaseAppConfig):
    project_name = 'Flourish'
    institution = 'Botswana-Harvard AIDS Institute'


class EdcDataManagerAppConfig(BaseEdcDataManagerAppConfig):
    identifier_pattern = None
    extra_assignee_choices = {}


class EdcProtocolAppConfig(BaseEdcProtocolAppConfig):
    protocol = ''
    protocol_name = 'Flourish'
    protocol_number = ''
    protocol_title = ''
    study_open_datetime = datetime(
        2020, 9, 16, 0, 0, 0, tzinfo=gettz('UTC'))
    study_close_datetime = datetime(
        2023, 12, 31, 23, 59, 59, tzinfo=gettz('UTC'))


class EdcTimepointAppConfig(BaseEdcTimepointAppConfig):
    timepoints = TimepointCollection(
        timepoints=[
            Timepoint(
                model='edc_appointment.appointment',
                datetime_field='appt_datetime',
                status_field='appt_status',
                closed_status=COMPLETE_APPT),
            Timepoint(
                model='edc_appointment.historicalappointment',
                datetime_field='appt_datetime',
                status_field='appt_status',
                closed_status=COMPLETE_APPT),
        ])