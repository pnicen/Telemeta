# Copyright (C) 2008 Parisson SARL
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution. The terms
# are also available at http://svn.parisson.org/telemeta/TelemetaLicense.
#
# Author: Guillaume Pellerin <yomguy@parisson.com>

from telemeta.analysis.core import *
from telemeta.analysis.api import IMediaItemAnalyzer
import numpy

class LengthAnalyzer(AudioProcessor):
    """Media item analyzer driver interface"""

    implements(IMediaItemAnalyzer)

    def __init__(self):
        self.fft_size = 2048
        self.window_function = numpy.hanning
        self.window = self.window_function(self.fft_size)
        
    def get_id(self):
        return "length"

    def get_name(self):
        return "Length"

    def get_unit(self):
        return "s"

    def render(self, media_item, options=None):
        self.pre_process(media_item)
        return numpy.round(numpy.divide(self.frames, self.samplerate),2)
