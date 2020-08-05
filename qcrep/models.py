from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from users.models import Profile
from PIL import Image

# Create your models here.
class Qcreport(models.Model):
    Result = (
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('Pending', 'Pending'),
    )
    Fps = (
        ('Pending', 'Pending'),
        ('23.98P', '23.98 Progressive'),
        ('23.98I', '23.98 Interlaced'),
        ('29.97P', '29.97 Progressive'),
        ('29.97I', '29.97 Interlaced'),
        ('25P', '25 Progressive'),
        ('25I', '25 Interlaced'),
        ('24P', '24 Progressive'),
        ('59.94I', '59.94I'),
    )
    Reject = (
        ('Pending', 'Pending'),
        ('MB', 'Macroblocks'),
        ('IF', 'Inverted Fields'),
        ('BF', 'Blended Fields'),
        ('BM', 'Broken Media'),
        ('VBI', 'VBI Line'),
        ('Sync', 'Out of sync'),
        ('RG', 'Red or Green Frames'),
        ('FF', 'Frezzed Frames'),
        ('RF', 'Repeated Frames'),
        ('AF', 'Artifacts'),
        ('SA', 'Saturated Audio'),
        ('WAM', 'Audio does not belong to media'),
        ('AN', 'Audio Noise'),
        ('Drop', 'Audio/Video Drop Out'),
        ('BR', 'Low Bit Rate'),
        ('VS', 'Video out or range or Standards'),
        ('None', 'None'),
    )
    MissElements = (
        ('MovieTitle', 'Movie Title'),
        ('Initial Credits', 'Initial Credits'),
        ('Final Roller', 'Final Roller'),
        ('Ep Num', 'Episode Number'),
        ('None', 'None'),
        ('Pending', 'Pending'),
    )

    title = models.CharField(max_length=100)
    client = models.CharField(max_length=100)
    filename = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default='Pending', choices = Result)
    aspect = models.CharField(max_length=100, default='Pending')
    codec = models.CharField(max_length=100, default='Pending')
    bit = models.CharField(max_length=100, default='Pending')
    resolution = models.CharField(max_length=100, default='Pending')
    date_posted = models.DateTimeField(default=timezone.now)
    qc_duedate = models.DateTimeField(default=timezone.now, blank=True)
    conmments = models.TextField(default='Pending')
    author = models.ForeignKey(User, default='None', on_delete=models.CASCADE)
    
    image = models.ImageField(default='image_penging.png', upload_to='qcreports_pics')
    framesPerSecond = models.CharField(max_length=100, default='Pending', choices = Fps)
    tecreject = models.CharField(max_length=100, default='Pending', choices = Reject)
    missing_elements = models.CharField(max_length=100, default='Pending', choices = MissElements)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('qcrep-qcreport_list')
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 720 or img.width > 480:
            output_size = (360, 2400)
            img.thumbnail(output_size)
            img.save(self.image.path)

    



class UsersChart(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    num_qcreports = models.IntegerField()

    def num_qcreports(request):
        num_qcreports = Qcreport.objects.filter(author=request.user).count()
        return render(request, 'user_reports.html', {'num_qcreports': num_qcreports})
        
    def __str_(self):
        return "{}-{}".format(self.author, self.num_qcreports)

    