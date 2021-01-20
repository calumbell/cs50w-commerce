from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    def __str__(self):
        return f"{self.username}"

class Auction(models.Model):
    item_name = models.CharField(max_length=64)
    item_description = models.CharField(max_length=800)
    start_bid = models.FloatField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="auctions")

    def __str__(self):
        return f"Auction #{self.id}: {self.name} ({self.user.username})"

class Bid(models.Model):
    amount = models.FloatField()
    time = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="bids")

    def __str__(self):
        return f"Bid #{self.id}: {self.amount} on {self.auction.item_name} by {self.user.username}"


class Comment(models.Model):
    message = models.CharField(max_length=255)
    time = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"Comment #{self.id}: {self.user.username} on {self.auction.item_name}: {self.message}"
