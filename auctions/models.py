from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator


class User(AbstractUser):
    def __str__(self):
        return f"{self.username}"

class Auction(models.Model):
    item_name = models.CharField(max_length=64)
    item_description = models.TextField(max_length=800)
    start_time = models.DateTimeField()
    start_bid = models.DecimalField(max_digits=7, decimal_places=2,
                                    validators=[MinValueValidator(0.01)])
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="auctions")

    def __str__(self):
        return f"Auction #{self.id}: {self.item_name} ({self.user.username})"

class Bid(models.Model):
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="bids")

    def __str__(self):
        return f"Bid #{self.id}: {self.amount} on {self.auction.item_name} by {self.user.username}"


class Comment(models.Model):
    message = models.TextField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"Comment #{self.id}: {self.user.username} on {self.auction.item_name}: {self.message}"
