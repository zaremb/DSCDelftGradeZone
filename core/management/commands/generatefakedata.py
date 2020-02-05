from faker import Faker
from faker.providers import person, profile, lorem, company
import random
import string

from django.core.management.base import BaseCommand, CommandError

from core.models import CustomUser, Course, Grade


class Command(BaseCommand):
    help = 'Generates fake data'


    def handle(self, *args, **options):

        fake = Faker()
        fake.add_provider(person)
        fake.add_provider(profile)
        fake.add_provider(lorem)
        fake.add_provider(company)

        for _ in range(60):
            profile_data = fake.simple_profile()
            CustomUser.objects.create_user(profile_data['username'], profile_data['mail'], ''.join(random.choice(string.ascii_letters) for _ in range(10)), first_name=fake.first_name(), last_name=fake.last_name())
        teachers = CustomUser.objects.all()[:10]
        students = CustomUser.objects.all()[10:]
        for i in range(10):
            course = Course(name=fake.bs(), code=''.join(random.choice(string.ascii_letters) for _ in range(2)), responsibleTeacher=teachers[i])
            course.save()

            random_student_ids = random.sample(list(students.values_list('id', flat=True)), 20)
            qs = CustomUser.objects.filter(id__in=random_student_ids)

            course.students.add(*qs)
            for student in qs:
                Grade(value=random.randint(10,100)/10, course=course, user=student).save()

        self.stdout.write(self.style.SUCCESS('Generated new users'))