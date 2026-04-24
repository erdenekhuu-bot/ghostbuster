from rest_framework import serializers
from .models import Location
from django.contrib.auth.models import User
from image.models import Image
from video.models import Video
from member.models import Member

class LocationMakeSerializer(serializers.ModelSerializer):
    image = serializers.ListField(
        child=serializers.ImageField(max_length=None, use_url=False),
        write_only=True,
        required=False
        
    )
    video = serializers.ListField(
        child=serializers.FileField(max_length=None, use_url=False),
        write_only=True,
        required=False
    )

    class Meta:
        model = Location
        fields = ['id','title','description','address','image','video']
        read_only_fields = ['id','image','video']
    
    
    def create(self, validated_data):
        images = validated_data.pop('image', [])
        videos = validated_data.pop('video', [])

        location = Location.objects.create(**validated_data)


        created_images = []
        for img_file in images:
            img = Image.objects.create(file=img_file)
            created_images.append(img)

        created_videos = []
        for vid_file in videos:
            v = Video.objects.create(file=vid_file)
            created_videos.append(v)

        if created_images:
            location.image = created_images[0]
        if created_videos:
            location.video = created_videos[0]
        location.save()

        return location


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username']

class MemberSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Member
        fields = ['id','user','phone','status']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'file']  

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id','file']

class LocationListSerializer(serializers.ModelSerializer):
    image = ImageSerializer(read_only=True)
    class Meta:
        model=Location
        fields=['id','title','address','image','video','created_at']

class LocationSerializer(serializers.ModelSerializer):
    image = ImageSerializer(read_only=True)
    video = VideoSerializer(read_only=True)

    images = ImageSerializer(source='image_set', many=True, read_only=True)
    videos = VideoSerializer(source='video_set', many=True, read_only=True)

    member = MemberSerializer(read_only=True) 

    class Meta:
        model = Location
        fields = ['id','title','description','address','member','image','video','images','videos','created_at']

