from django.db import models

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    duration = models.IntegerField()  # Kurs davomiyligi (masalan, haftalar soni)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    full_price = models.DecimalField(max_digits=15, decimal_places=2)
    pay_later = models.DecimalField(max_digits=15, decimal_places=2)
    after_course = models.TextField()
    discount = models.IntegerField()
    discount_place = models.IntegerField()
    image = models.ImageField(upload_to='courses/', default='courses/course_python.jpg')


    def __str__(self):
        return self.name


class School(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    discount = models.IntegerField()
    discount_place = models.IntegerField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(upload_to='images/')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class Registration(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.course.name}"
    




# Rus tili vaqtunchalik

class CourseRu(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    duration = models.IntegerField()  # Kurs davomiyligi (masalan, haftalar soni)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    full_price = models.DecimalField(max_digits=15, decimal_places=2)
    pay_later = models.DecimalField(max_digits=15, decimal_places=2)
    after_course = models.TextField()
    discount = models.IntegerField()
    discount_place = models.IntegerField()
    image = models.ImageField(upload_to='courses/', default='courses/course_python.jpg')


    def __str__(self):
        return self.name


class SchoolRu(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    discount = models.IntegerField()
    discount_place = models.IntegerField()

    def __str__(self):
        return self.name


class CommentRu(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(upload_to='images/')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class TeacherRu(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name
    

# Ingliz tili vaqtunchalik

class CourseEn(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    duration = models.IntegerField()  # Kurs davomiyligi (masalan, haftalar soni)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    full_price = models.DecimalField(max_digits=15, decimal_places=2)
    pay_later = models.DecimalField(max_digits=15, decimal_places=2)
    after_course = models.TextField()
    discount = models.IntegerField()
    discount_place = models.IntegerField()
    image = models.ImageField(upload_to='courses/', default='courses/course_python.jpg')

    def __str__(self):
        return self.name
    

class SchoolEn(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    discount = models.IntegerField()
    discount_place = models.IntegerField()

    def __str__(self):
        return self.name
    

class CommentEn(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(upload_to='images/')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class TeacherEn(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name