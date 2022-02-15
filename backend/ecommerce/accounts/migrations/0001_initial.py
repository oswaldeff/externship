# Generated by Django 3.2 on 2022-01-14 17:58

import accounts.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='생성날짜')),
                ('updated', models.DateField(auto_now=True, verbose_name='업데이트날짜')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='아이디')),
                ('password', models.CharField(max_length=255, verbose_name='비밀번호')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='이메일')),
                ('is_seller', models.BooleanField(default=False, verbose_name='셀러')),
                ('brand', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='브랜드')),
                ('is_active', models.BooleanField(default=True, verbose_name='활성화')),
                ('is_staff', models.BooleanField(default=False, verbose_name='스태프')),
                ('is_admin', models.BooleanField(default=False, verbose_name='어드민')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='슈퍼유저')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': '1. 전체유저 목록',
                'db_table': 'users',
            },
            managers=[
                ('objects', accounts.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='PhoneVerification',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='생성날짜')),
                ('updated', models.DateField(auto_now=True, verbose_name='업데이트날짜')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('phone_number', models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator('^\\d{3}-?[1-9]\\d{3}-?\\d{4}$')], verbose_name='휴대폰 번호')),
                ('verification_code', models.CharField(max_length=255, verbose_name='인증번호')),
                ('is_verified', models.BooleanField(default=False, verbose_name='인증')),
                ('is_used', models.BooleanField(default=False, verbose_name='가입')),
            ],
            options={
                'verbose_name_plural': '4. 휴대폰번호 인증 목록',
                'db_table': 'phone_verifications',
            },
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='생성날짜')),
                ('updated', models.DateField(auto_now=True, verbose_name='업데이트날짜')),
                ('phone_number', models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator('^\\d{3}-?[1-9]\\d{3}-?\\d{4}$')], verbose_name='휴대폰 번호')),
                ('brand', models.CharField(max_length=255, verbose_name='브랜드')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '3. 셀러 목록',
                'db_table': 'sellers',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='생성날짜')),
                ('updated', models.DateField(auto_now=True, verbose_name='업데이트날짜')),
                ('phone_number', models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator('^\\d{3}-?[1-9]\\d{3}-?\\d{4}$')], verbose_name='휴대폰 번호')),
                ('is_local', models.BooleanField(default=False, verbose_name='로컬계정')),
                ('connect_social', models.BooleanField(default=False, verbose_name='소셜계정')),
                ('social_type', models.CharField(blank=True, max_length=8, null=True, verbose_name='소셜타입')),
                ('social_id', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='소셜계정 고유식별값')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '2. 커스토머 목록',
                'db_table': 'customers',
            },
        ),
    ]
