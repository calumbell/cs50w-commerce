from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator
from datetime import datetime, timedelta

class User(AbstractUser):
    def __str__(self):
        return f"{self.username}"

class Auction(models.Model):
    DURATIONS = (
        (3, "Three Days"),
        (7, "One Week"),
        (14, "Two Weeks"),
        (28, "Four Weeks")
    )

    item_name        = models.CharField(max_length=64)
    item_description = models.TextField(max_length=800)
    start_time       = models.DateTimeField()
    end_time         = models.DateTimeField()
    duration         = models.IntegerField(choices=DURATIONS)
    ended_manually   = models.BooleanField(default=False)
    start_bid        = models.DecimalField(max_digits=7, decimal_places=2,
                                            validators=[MinValueValidator(0.01)])

    user             = models.ForeignKey(User, on_delete=models.CASCADE,
                                            related_name="auctions")

    watchers         = models.ManyToManyField(User, blank=True,
                                                related_name="watchlist")


    def __str__(self):
        return f"Auction #{self.id}: {self.item_name} ({self.user.username})"

    def save(self, *args, **kwargs):
        self.start_time = datetime.now()
        self.end_time = self.start_time + timedelta(days=self.duration)
        super().save(*args, **kwargs) # call existing save() method


class Bid(models.Model):
    amount  = models.DecimalField(max_digits=7, decimal_places=2)
    user    = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="bids")

    class Meta:
        ordering = ('-amount',)

    def __str__(self):
        return f"Bid #{self.id}: {self.amount} on {self.auction.item_name} by {self.user.username}"


class Comment(models.Model):
    message = models.TextField(max_length=255)
    time    = models.DateTimeField(auto_now_add=True)
    user    = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"Comment #{self.id}: {self.user.username} on {self.auction.item_name}: {self.message}"
