# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals

from mooquant.optimizer import worker

import rsi2

# The if __name__ == '__main__' part is necessary if running on Windows.
if __name__ == '__main__':
    worker.run(rsi2.RSI2, "localhost", 5000, workerName="localworker")
