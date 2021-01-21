from django.forms import ModelForm, TextInput
from .models import Auction

class AuctionForm(ModelForm):
    class Meta:
        model = Auction
        fields = ['item_name',
                  'item_description',
                  'start_bid']

    def __init__(self, *args, **kwargs):
        super(AuctionForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
