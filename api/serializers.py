from rest_framework import serializers
from .models import Course, School, Comment, Teacher, Registration
from .models import CourseEn, SchoolEn, CommentEn, TeacherEn
from .models import CourseRu, SchoolRu, CommentRu, TeacherRu

class CourseSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)  # Course modelidagi image maydoni

    class Meta:
        model = Course
        fields = '__all__'


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)  # Comment modelidagi image maydoni

    class Meta:
        model = Comment
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)  # Teacher modelidagi image maydoni

    class Meta:
        model = Teacher
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'


# Rus tili vaqtunchalik
class CourseRuSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseRu
        fields = '__all__'


class SchoolRuSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolRu
        fields = '__all__'


class CommentRuSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentRu
        fields = '__all__'


class TeacherRuSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherRu
        fields = '__all__'

# Ingliz tili vaqtunchalik

class CourseEnSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseEn
        fields = '__all__'


class SchoolEnSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolEn
        fields = '__all__'


class CommentEnSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentEn
        fields = '__all__'

class TeacherEnSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherEn
        fields = '__all__'