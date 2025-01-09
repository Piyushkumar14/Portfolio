# management/commands/fix_uuids.py
from django.core.management.base import BaseCommand
from base.models import Skill
import uuid


class Command(BaseCommand):
    help = 'Fix malformed UUIDs in the Skill model'

    def handle(self, *args, **kwargs):
        skills = Skill.objects.all()
        for skill in skills:
            try:
                # Try to convert the current id to a UUID
                uuid.UUID(str(skill.id))
            except ValueError:
                # If it fails, generate a new UUID and save it
                skill.id = uuid.uuid4()
                skill.save()
                self.stdout.write(self.style.SUCCESS(f'Fixed UUID for skill: {skill.title}'))
        self.stdout.write(self.style.SUCCESS('All malformed UUIDs have been fixed'))