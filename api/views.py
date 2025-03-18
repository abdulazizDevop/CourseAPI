# views.py
from rest_framework import status, permissions, generics

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Course, School, Comment, Teacher, Registration
from .models import CourseRu, SchoolRu, CommentRu, TeacherRu
from .models import CourseEn, SchoolEn, CommentEn, TeacherEn

from .serializers import CourseSerializer, SchoolSerializer, CommentSerializer, TeacherSerializer, RegistrationSerializer
from .serializers import CourseRuSerializer, SchoolRuSerializer, CommentRuSerializer, TeacherRuSerializer
from .serializers import CourseEnSerializer, SchoolEnSerializer, CommentEnSerializer, TeacherEnSerializer


class RegisterDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class SchoolDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class SchoolListView(generics.ListAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class CommentListView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class TeacherListView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class RegisterListView(generics.ListAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer


@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Ro'yxatdan o\'tish muvaffaqiyatli amalga oshirildi!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


# Rus tili vaqtunchalik
class CourseRuListView(generics.ListAPIView):
    queryset = CourseRu.objects.all()
    serializer_class = CourseRuSerializer

class SchoolRuListView(generics.ListAPIView):
    queryset = SchoolRu.objects.all()
    serializer_class = SchoolRuSerializer

class CommentRuListView(generics.ListAPIView):
    queryset = CommentRu.objects.all()
    serializer_class = CommentRuSerializer

class TeacherRuListView(generics.ListAPIView):
    queryset = TeacherRu.objects.all()
    serializer_class = TeacherRuSerializer


class CourseRuDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = CourseRu.objects.all()
    serializer_class = CourseRuSerializer

class SchoolRuDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = SchoolRu.objects.all()
    serializer_class = SchoolRuSerializer

class CommentRuDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = CommentRu.objects.all()
    serializer_class = CommentRuSerializer

class TeacherRuDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = TeacherRu.objects.all()
    serializer_class = TeacherRuSerializer


# Ingliz tili vaqtunchalik

class CourseEnListView(generics.ListAPIView):
    queryset = CourseEn.objects.all()
    serializer_class = CourseEnSerializer

class SchoolEnListView(generics.ListAPIView):
    queryset = SchoolEn.objects.all()
    serializer_class = SchoolEnSerializer

class CommentEnListView(generics.ListAPIView):
    queryset = CommentEn.objects.all()
    serializer_class = CommentEnSerializer

class TeacherEnListView(generics.ListAPIView):
    queryset = TeacherEn.objects.all()
    serializer_class = TeacherEnSerializer


class CourseEnDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = CourseEn.objects.all()
    serializer_class = CourseEnSerializer

class SchoolEnDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = SchoolEn.objects.all()
    serializer_class = SchoolEnSerializer

class CommentEnDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = CommentEn.objects.all()
    serializer_class = CommentEnSerializer

class TeacherEnDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = TeacherEn.objects.all()
    serializer_class = TeacherEnSerializer