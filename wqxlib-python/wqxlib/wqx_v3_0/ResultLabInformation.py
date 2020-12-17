from typing import List
from yattag import Doc, indent
from .DetectionQuantitationLimit import DetectionQuantitationLimit
from .SimpleContent import (
  LaboratoryName,
  AnalysisStartDate,
  AnalysisEndDate,
  LaboratoryCommentText,
  LaboratorySampleSplitRatio,
  LaboratoryAccreditationIndicator,
  LaboratoryAccreditationAuthorityName,
  TaxonomistAccreditationIndicator,
  TaxonomistAccreditationAuthorityName
)
from .WQXTime import WQXTime

class ResultLabInformation:
  """Describes information obtained by a laboratory related to a specific laboratory analysis."""

  __laboratoryName: LaboratoryName
  __analysisStartDate: AnalysisStartDate
  __analysisStartTime: WQXTime
  __analysisEndDate: AnalysisEndDate
  __analysisEndTime: WQXTime
  __laboratoryCommentText: LaboratoryCommentText
  __resultDetectionQuantitationLimit: DetectionQuantitationLimit
  __laboratorySampleSplitRatio: LaboratorySampleSplitRatio
  __laboratoryAccreditationIndicator: LaboratoryAccreditationIndicator
  __laboratoryAccreditationAuthorityName: LaboratoryAccreditationAuthorityName
  __taxonomistAccreditationIndicator: TaxonomistAccreditationIndicator
  __taxonomistAccreditationAuthorityName: TaxonomistAccreditationAuthorityName

  def __init__(self):
    self.__laboratoryName = None
    self.__analysisStartDate = None
    self.__analysisStartTime = None
    self.__analysisEndDate = None
    self.__analysisEndTime = None
    self.__laboratoryCommentText = None
    self.__resultDetectionQuantitationLimit = None
    self.__laboratorySampleSplitRatio = None
    self.__laboratoryAccreditationIndicator = None
    self.__laboratoryAccreditationAuthorityName = None
    self.__taxonomistAccreditationIndicator = None
    self.__taxonomistAccreditationAuthorityName = None

  @property
  def laboratoryName(self) -> LaboratoryName:
    return self.__laboratoryName
  @laboratoryName.setter
  def laboratoryName(self, val:LaboratoryName) -> None:
    self.__laboratoryName = None if val is None else LaboratoryName(val)

  @property
  def analysisStartDate(self) -> AnalysisStartDate:
    return self.__analysisStartDate
  @analysisStartDate.setter
  def analysisStartDate(self, val:AnalysisStartDate) -> None:
    self.__analysisStartDate = None if val is None else AnalysisStartDate(val)

  @property
  def analysisStartTime(self) -> WQXTime:
    """The local time and relative time zone when the analysis began."""
    return self.__analysisStartTime
  @analysisStartTime.setter
  def analysisStartTime(self, val:WQXTime) -> None:
    """The local time and relative time zone when the analysis began."""
    self.__analysisStartTime = None if val is None else WQXTime(val)

  @property
  def analysisEndDate(self) -> AnalysisEndDate:
    return self.__analysisEndDate
  @analysisEndDate.setter
  def analysisEndDate(self, val:AnalysisEndDate) -> None:
    self.__analysisEndDate = None if val is None else AnalysisEndDate(val)

  @property
  def analysisEndTime(self) -> WQXTime:
    """The local time and relative time zone when the analysis was finished."""
    return self.__analysisEndTime
  @analysisEndTime.setter
  def analysisEndTime(self, val:WQXTime) -> None:
    """The local time and relative time zone when the analysis was finished."""
    self.__analysisEndTime = None if val is None else WQXTime(val)

  @property
  def laboratoryCommentText(self) -> LaboratoryCommentText:
    return self.__laboratoryCommentText
  @laboratoryCommentText.setter
  def laboratoryCommentText(self, val:LaboratoryCommentText) -> None:
    self.__laboratoryCommentText = None if val is None else LaboratoryCommentText(val)

  @property
  def resultDetectionQuantitationLimit(self) -> List[DetectionQuantitationLimit]:
    """Information that describes one of a variety of detection or quantitation limits determined in a laboratory."""
    return self.__resultDetectionQuantitationLimit
  @resultDetectionQuantitationLimit.setter
  def resultDetectionQuantitationLimit(self, val:List[DetectionQuantitationLimit]) -> None:
    """Information that describes one of a variety of detection or quantitation limits determined in a laboratory."""
    if not isinstance(val, list):
      raise TypeError("Attribute resultDetectionQuantitationLimit must be a list of 0 or more values.")
    self.__resultDetectionQuantitationLimit = val

  @property
  def laboratorySampleSplitRatio(self) -> LaboratorySampleSplitRatio:
    return self.__laboratorySampleSplitRatio
  @laboratorySampleSplitRatio.setter
  def laboratorySampleSplitRatio(self, val:LaboratorySampleSplitRatio) -> None:
    self.__laboratorySampleSplitRatio = None if val is None else LaboratorySampleSplitRatio(val)

  @property
  def laboratoryAccreditationIndicator(self) -> LaboratoryAccreditationIndicator:
    return self.__laboratoryAccreditationIndicator
  @laboratoryAccreditationIndicator.setter
  def laboratoryAccreditationIndicator(self, val:LaboratoryAccreditationIndicator) -> None:
    self.__laboratoryAccreditationIndicator = None if val is None else LaboratoryAccreditationIndicator(val)

  @property
  def laboratoryAccreditationAuthorityName(self) -> LaboratoryAccreditationAuthorityName:
    return self.__laboratoryAccreditationAuthorityName
  @laboratoryAccreditationAuthorityName.setter
  def laboratoryAccreditationAuthorityName(self, val:LaboratoryAccreditationAuthorityName) -> None:
    self.__laboratoryAccreditationAuthorityName = None if val is None else LaboratoryAccreditationAuthorityName(val)

  @property
  def taxonomistAccreditationIndicator(self) -> TaxonomistAccreditationIndicator:
    return self.__taxonomistAccreditationIndicator
  @taxonomistAccreditationIndicator.setter
  def taxonomistAccreditationIndicator(self, val:TaxonomistAccreditationIndicator) -> None:
    self.__taxonomistAccreditationIndicator = None if val is None else TaxonomistAccreditationIndicator(val)

  @property
  def taxonomistAccreditationAuthorityName(self) -> TaxonomistAccreditationAuthorityName:
    return self.__taxonomistAccreditationAuthorityName
  @taxonomistAccreditationAuthorityName.setter
  def taxonomistAccreditationAuthorityName(self, val:TaxonomistAccreditationAuthorityName) -> None:
    self.__taxonomistAccreditationAuthorityName = None if val is None else TaxonomistAccreditationAuthorityName(val)

  def generateXML(self):
    doc, tag, text, line = Doc().ttl()

    if self.__laboratoryName is not None:
      line('LaboratoryName', self.__laboratoryName)
    if self.__analysisStartDate is not None:
      line('AnalysisStartDate', self.__analysisStartDate)
    if self.__analysisStartTime is not None:
      line('WQXTime', self.__analysisStartTime)
    if self.__analysisEndDate is not None:
      line('AnalysisEndDate', self.__analysisEndDate)
    if self.__analysisEndTime is not None:
      line('WQXTime', self.__analysisEndTime)
    if self.__laboratoryCommentText is not None:
      line('LaboratoryCommentText', self.__laboratoryCommentText)
    for x in self.__resultDetectionQuantitationLimit:
      line('DetectionQuantitationLimit', x)
    if self.__laboratorySampleSplitRatio is not None:
      line('LaboratorySampleSplitRatio', self.__laboratorySampleSplitRatio)
    if self.__laboratoryAccreditationIndicator is not None:
      line('LaboratoryAccreditationIndicator', self.__laboratoryAccreditationIndicator)
    if self.__laboratoryAccreditationAuthorityName is not None:
      line('LaboratoryAccreditationAuthorityName', self.__laboratoryAccreditationAuthorityName)
    if self.__taxonomistAccreditationIndicator is not None:
      line('TaxonomistAccreditationIndicator', self.__taxonomistAccreditationIndicator)
    if self.__taxonomistAccreditationAuthorityName is not None:
      line('TaxonomistAccreditationAuthorityName', self.__taxonomistAccreditationAuthorityName)

    return indent(doc.getvalue(), indentation = ' '*2)
