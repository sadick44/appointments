from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Adding users in tale User"

    def handle(self, *args, **options):
        # Making all the commercials as superuser and giving them all the privileges

        users = [
            {"first_name" :"François", "last_name": "Pignon","email": "francois.pignon@dinner.con",
             "password": "password"},
            {"first_name" :"Juste", "last_name": "Leblanc", "email": "juste.leblanc@dinner.con",
             "password": "password"},
            {"first_name" :"Marlène", "last_name": "Sassoeur","email": "marlen.sassoeur@dinner.con",
             "password": "password"}]

        for user in users:
            u = User.objects.create(
                first_name=user["first_name"],
                last_name=user["last_name"],
                email=user["email"],
                password=user["password"],
                username=user["first_name"]+user["last_name"],
                is_staff=True,
                is_superuser=True
            )

            u.save()

        return