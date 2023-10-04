from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class KHAINIEM(models.Model):
    MA_KNIEM = models.TextField()
    TEN_KTHUC = models.TextField()
    TU_KHOA = models.TextField()
    ND_KTHUC = models.TextField()
    MA_LKET = models.TextField()

    def __str__(self):
        return f"{self.MA_KNIEM} - {self.TEN_KTHUC} - {self.ND_KTHUC}"

    def get_ma_kniem(self):
        return self.MA_KNIEM

    def get_ten_kthuc(self):
        return self.TEN_KTHUC

    def get_ten_kthuc(self):
        return self.ND_KTHUC


class BAITAP(models.Model):
    MA_BT = models.TextField()
    TOM_TAT = models.TextField()
    MA_KN = models.TextField()
    TEN_KTHUC = models.TextField()

    def __str__(self):
        return f"{self.MA_BT} - {self.TOM_TAT} - {self.MA_KN} - {self.TEN_KTHUC}"

    def get_ma_bt(self):
        return self.MA_BT

    def get_tomtat(self):
        return self.TOM_TAT

    def get_makn(self):
        return self.MA_KN

    def get_ten_kthuc(self):
        return self.TEN_KTHUC

"""
class KHAINIEM_BAITAP(models.Model):
    khainiem = models.ForeignKey(KHAINIEM, on_delete=models.CASCADE)
    baitap = models.ForeignKey(BAITAP, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.khainiem.TEN_KTHUC} - {self.baitap.TEN_KTHUC}"

    class Meta:
        # Define a composite primary key to prevent duplicate pairs
        unique_together = ('khainiem', 'baitap')"""