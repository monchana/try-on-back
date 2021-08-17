from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=False,
        verbose_name="생성 일시",
        help_text="데이터가 생성된 날짜입니다.",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=False,
        verbose_name="수정 일시",
        help_text="데이터가 수정된 날짜입니다.",
    )

    class Meta:
        abstract = True


class BaseActiveModel(models.Model):
    is_active = models.BooleanField(
        default=True,
        db_index=True,
        verbose_name="활성화 여부",
        help_text="활성화할지 여부를 결정합니다.",
    )

    class Meta:
        abstract = True


class GenderModel(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, default="F")

    class Meta:
        abstract = True
