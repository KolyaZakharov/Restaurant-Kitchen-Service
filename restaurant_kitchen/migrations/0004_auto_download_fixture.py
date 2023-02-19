
from django.core.management import call_command
from django.db import migrations


def load_fixtures(state, schema_editor):
    call_command("loaddata", "rest_data.json")


def reverse_load_fixtures(state, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ("restaurant_kitchen", "0003_alter_cook_first_name_alter_cook_last_name"),
    ]

    operations = [
        migrations.RunPython(load_fixtures, reverse_load_fixtures)
    ]
