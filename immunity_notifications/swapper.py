from swapper import load_model as swapper_load_model

from immunity_notifications.apps import ImmunityNotificationsConfig as AppConfig


def load_model(model):
    return swapper_load_model(AppConfig.label, model)
