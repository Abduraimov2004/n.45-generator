from typing import Optional


class Range:
    """
      Range klassi berilgan boshi - (start), oxiri - (stop) va qadam - (step)

      Step parametri float bo'la oladi

      Agar faqat bitta argument berilsa bu argument (stop) qiymatiga teng bo'ladi va start 0 ga teng bo'ladi

      start (int): Intervalning boshlanishi
      stop (int, optional): Intervalning tugashi
      step (int, optional): Qadam
      """
    def __init__(self, start: int, stop: Optional[int] = None, step: Optional[float] = int):
        if stop is None:
            self.stop = start
            self.start = -step
            self.step = step
        else:
            self.start = start - step
            self.stop = stop
            self.step = step

    def __iter__(self) -> Optional[object]:
        return self

    def __next__(self) -> object:
        if self.start > self.stop and self.step > 0:
            raise StopIteration

        elif self.start > self.stop and self.step < 0:
            self.start += self.step
            if self.stop >= self.start:
                raise StopIteration
            return self.start

        elif self.start < self.stop and self.step > 0:
            self.start += self.step
            if self.start >= self.stop:
                raise StopIteration
            return self.start



for i in Range(16, 5, -2.2):
    print(round(i, 1))
