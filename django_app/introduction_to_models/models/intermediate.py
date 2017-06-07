from django.db import models
from django.utils import timezone


class Player(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    # current_club프로퍼티에 현재 속하는 Club 리턴
    @property
    def current_club(self):
        return self.club_set.get(tradeinfo__date_leaved__isnull=True).name

    # current_tradeinfo프로퍼티에 현재 자신의 TradeInfo리턴
    @property
    def current_tradeinfo(self):
        return TradeInfo.objects.get(player=self)

class Club(models.Model):
    name = models.CharField(max_length=40)
    players = models.ManyToManyField(
        Player,
        through='TradeInfo',
        # through_fields=('player', 'club')
    )

    def __str__(self):
        return self.name

    def squad(self, year=None):
        if year:
            self.players.filter(
                tradeinfo__date_joined__lte=(year, 1, 1),
                # tradeinfo__date_leaved__lte=(year, 12, 31),
            )
        else:
            self.players.filter(tradeinfo__date_joined__lte=timezone.now())
            # squad 매서드에 현직 선수들만 리턴
            # 인수로 년도(2017, 2015 등)을 받아 해당 년도의 현직 선수들을 리턴,
            # 주어지지지 않으면 현재를 기준으로 함


class TradeInfo(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    date_joined = models.DateField()
    date_leaved = models.DateField(null=True, blank=True)
    # recommender = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, blank=True)
    # prev_club = 이전 Club
    # prev_club = models.ForeignKey(Club, on_delete=models.CASCADE, null=True, blank=True)

    # property로 is_current 속성이 TradeInfo가 현재 현직(leaved하지 않았는지)
    # recommender와 prev_club을 활성화 시키고 Club의 MTM필드에 through_fields를 명시
    @property
    def is_current(self):
        return self.date_leaved is None
