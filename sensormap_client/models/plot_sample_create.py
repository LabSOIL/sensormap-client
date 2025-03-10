# coding: utf-8

"""
    soil-api

    API for managing SOIL lab data

    The version of the OpenAPI document: 2.1.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class PlotSampleCreate(BaseModel):
    """
    PlotSampleCreate
    """ # noqa: E501
    al_ug_per_g: Optional[Union[StrictFloat, StrictInt]] = None
    archea_per_g: Optional[Union[StrictFloat, StrictInt]] = None
    bacteria_per_g: Optional[Union[StrictFloat, StrictInt]] = None
    c: Optional[Union[StrictFloat, StrictInt]] = None
    ca_ug_per_g: Optional[Union[StrictFloat, StrictInt]] = None
    cl_ug_per_g: Optional[Union[StrictFloat, StrictInt]] = None
    clay_percent: Optional[Union[StrictFloat, StrictInt]] = None
    cn: Optional[Union[StrictFloat, StrictInt]] = None
    fe_ug_per_g: Optional[Union[StrictFloat, StrictInt]] = None
    fungi_per_g: Optional[Union[StrictFloat, StrictInt]] = None
    k_ug_per_g: Optional[Union[StrictFloat, StrictInt]] = None
    loi: Optional[Union[StrictFloat, StrictInt]] = None
    lower_depth_cm: Union[StrictFloat, StrictInt]
    methanogens_per_g: Optional[Union[StrictFloat, StrictInt]] = None
    methanotrophs_per_g: Optional[Union[StrictFloat, StrictInt]] = None
    mfc: Optional[Union[StrictFloat, StrictInt]] = None
    mg_ug_per_g: Optional[Union[StrictFloat, StrictInt]] = None
    mn_ug_per_g: Optional[Union[StrictFloat, StrictInt]] = None
    n: Optional[Union[StrictFloat, StrictInt]] = None
    na_ug_per_g: Optional[Union[StrictFloat, StrictInt]] = None
    name: StrictStr
    p_ug_per_g: Optional[Union[StrictFloat, StrictInt]] = None
    ph: Optional[Union[StrictFloat, StrictInt]] = None
    plot_id: StrictStr
    replicate: StrictInt
    rh: Optional[Union[StrictFloat, StrictInt]] = None
    s_ug_per_g: Optional[Union[StrictFloat, StrictInt]] = None
    sample_weight: Optional[Union[StrictFloat, StrictInt]] = None
    sand_percent: Optional[Union[StrictFloat, StrictInt]] = None
    si_ug_per_g: Optional[Union[StrictFloat, StrictInt]] = None
    silt_percent: Optional[Union[StrictFloat, StrictInt]] = None
    subsample_replica_weight: Optional[Union[StrictFloat, StrictInt]] = None
    subsample_weight: Optional[Union[StrictFloat, StrictInt]] = None
    upper_depth_cm: Union[StrictFloat, StrictInt]
    __properties: ClassVar[List[str]] = ["al_ug_per_g", "archea_per_g", "bacteria_per_g", "c", "ca_ug_per_g", "cl_ug_per_g", "clay_percent", "cn", "fe_ug_per_g", "fungi_per_g", "k_ug_per_g", "loi", "lower_depth_cm", "methanogens_per_g", "methanotrophs_per_g", "mfc", "mg_ug_per_g", "mn_ug_per_g", "n", "na_ug_per_g", "name", "p_ug_per_g", "ph", "plot_id", "replicate", "rh", "s_ug_per_g", "sample_weight", "sand_percent", "si_ug_per_g", "silt_percent", "subsample_replica_weight", "subsample_weight", "upper_depth_cm"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of PlotSampleCreate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if al_ug_per_g (nullable) is None
        # and model_fields_set contains the field
        if self.al_ug_per_g is None and "al_ug_per_g" in self.model_fields_set:
            _dict['al_ug_per_g'] = None

        # set to None if archea_per_g (nullable) is None
        # and model_fields_set contains the field
        if self.archea_per_g is None and "archea_per_g" in self.model_fields_set:
            _dict['archea_per_g'] = None

        # set to None if bacteria_per_g (nullable) is None
        # and model_fields_set contains the field
        if self.bacteria_per_g is None and "bacteria_per_g" in self.model_fields_set:
            _dict['bacteria_per_g'] = None

        # set to None if c (nullable) is None
        # and model_fields_set contains the field
        if self.c is None and "c" in self.model_fields_set:
            _dict['c'] = None

        # set to None if ca_ug_per_g (nullable) is None
        # and model_fields_set contains the field
        if self.ca_ug_per_g is None and "ca_ug_per_g" in self.model_fields_set:
            _dict['ca_ug_per_g'] = None

        # set to None if cl_ug_per_g (nullable) is None
        # and model_fields_set contains the field
        if self.cl_ug_per_g is None and "cl_ug_per_g" in self.model_fields_set:
            _dict['cl_ug_per_g'] = None

        # set to None if clay_percent (nullable) is None
        # and model_fields_set contains the field
        if self.clay_percent is None and "clay_percent" in self.model_fields_set:
            _dict['clay_percent'] = None

        # set to None if cn (nullable) is None
        # and model_fields_set contains the field
        if self.cn is None and "cn" in self.model_fields_set:
            _dict['cn'] = None

        # set to None if fe_ug_per_g (nullable) is None
        # and model_fields_set contains the field
        if self.fe_ug_per_g is None and "fe_ug_per_g" in self.model_fields_set:
            _dict['fe_ug_per_g'] = None

        # set to None if fungi_per_g (nullable) is None
        # and model_fields_set contains the field
        if self.fungi_per_g is None and "fungi_per_g" in self.model_fields_set:
            _dict['fungi_per_g'] = None

        # set to None if k_ug_per_g (nullable) is None
        # and model_fields_set contains the field
        if self.k_ug_per_g is None and "k_ug_per_g" in self.model_fields_set:
            _dict['k_ug_per_g'] = None

        # set to None if loi (nullable) is None
        # and model_fields_set contains the field
        if self.loi is None and "loi" in self.model_fields_set:
            _dict['loi'] = None

        # set to None if methanogens_per_g (nullable) is None
        # and model_fields_set contains the field
        if self.methanogens_per_g is None and "methanogens_per_g" in self.model_fields_set:
            _dict['methanogens_per_g'] = None

        # set to None if methanotrophs_per_g (nullable) is None
        # and model_fields_set contains the field
        if self.methanotrophs_per_g is None and "methanotrophs_per_g" in self.model_fields_set:
            _dict['methanotrophs_per_g'] = None

        # set to None if mfc (nullable) is None
        # and model_fields_set contains the field
        if self.mfc is None and "mfc" in self.model_fields_set:
            _dict['mfc'] = None

        # set to None if mg_ug_per_g (nullable) is None
        # and model_fields_set contains the field
        if self.mg_ug_per_g is None and "mg_ug_per_g" in self.model_fields_set:
            _dict['mg_ug_per_g'] = None

        # set to None if mn_ug_per_g (nullable) is None
        # and model_fields_set contains the field
        if self.mn_ug_per_g is None and "mn_ug_per_g" in self.model_fields_set:
            _dict['mn_ug_per_g'] = None

        # set to None if n (nullable) is None
        # and model_fields_set contains the field
        if self.n is None and "n" in self.model_fields_set:
            _dict['n'] = None

        # set to None if na_ug_per_g (nullable) is None
        # and model_fields_set contains the field
        if self.na_ug_per_g is None and "na_ug_per_g" in self.model_fields_set:
            _dict['na_ug_per_g'] = None

        # set to None if p_ug_per_g (nullable) is None
        # and model_fields_set contains the field
        if self.p_ug_per_g is None and "p_ug_per_g" in self.model_fields_set:
            _dict['p_ug_per_g'] = None

        # set to None if ph (nullable) is None
        # and model_fields_set contains the field
        if self.ph is None and "ph" in self.model_fields_set:
            _dict['ph'] = None

        # set to None if rh (nullable) is None
        # and model_fields_set contains the field
        if self.rh is None and "rh" in self.model_fields_set:
            _dict['rh'] = None

        # set to None if s_ug_per_g (nullable) is None
        # and model_fields_set contains the field
        if self.s_ug_per_g is None and "s_ug_per_g" in self.model_fields_set:
            _dict['s_ug_per_g'] = None

        # set to None if sample_weight (nullable) is None
        # and model_fields_set contains the field
        if self.sample_weight is None and "sample_weight" in self.model_fields_set:
            _dict['sample_weight'] = None

        # set to None if sand_percent (nullable) is None
        # and model_fields_set contains the field
        if self.sand_percent is None and "sand_percent" in self.model_fields_set:
            _dict['sand_percent'] = None

        # set to None if si_ug_per_g (nullable) is None
        # and model_fields_set contains the field
        if self.si_ug_per_g is None and "si_ug_per_g" in self.model_fields_set:
            _dict['si_ug_per_g'] = None

        # set to None if silt_percent (nullable) is None
        # and model_fields_set contains the field
        if self.silt_percent is None and "silt_percent" in self.model_fields_set:
            _dict['silt_percent'] = None

        # set to None if subsample_replica_weight (nullable) is None
        # and model_fields_set contains the field
        if self.subsample_replica_weight is None and "subsample_replica_weight" in self.model_fields_set:
            _dict['subsample_replica_weight'] = None

        # set to None if subsample_weight (nullable) is None
        # and model_fields_set contains the field
        if self.subsample_weight is None and "subsample_weight" in self.model_fields_set:
            _dict['subsample_weight'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PlotSampleCreate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "al_ug_per_g": obj.get("al_ug_per_g"),
            "archea_per_g": obj.get("archea_per_g"),
            "bacteria_per_g": obj.get("bacteria_per_g"),
            "c": obj.get("c"),
            "ca_ug_per_g": obj.get("ca_ug_per_g"),
            "cl_ug_per_g": obj.get("cl_ug_per_g"),
            "clay_percent": obj.get("clay_percent"),
            "cn": obj.get("cn"),
            "fe_ug_per_g": obj.get("fe_ug_per_g"),
            "fungi_per_g": obj.get("fungi_per_g"),
            "k_ug_per_g": obj.get("k_ug_per_g"),
            "loi": obj.get("loi"),
            "lower_depth_cm": obj.get("lower_depth_cm"),
            "methanogens_per_g": obj.get("methanogens_per_g"),
            "methanotrophs_per_g": obj.get("methanotrophs_per_g"),
            "mfc": obj.get("mfc"),
            "mg_ug_per_g": obj.get("mg_ug_per_g"),
            "mn_ug_per_g": obj.get("mn_ug_per_g"),
            "n": obj.get("n"),
            "na_ug_per_g": obj.get("na_ug_per_g"),
            "name": obj.get("name"),
            "p_ug_per_g": obj.get("p_ug_per_g"),
            "ph": obj.get("ph"),
            "plot_id": obj.get("plot_id"),
            "replicate": obj.get("replicate"),
            "rh": obj.get("rh"),
            "s_ug_per_g": obj.get("s_ug_per_g"),
            "sample_weight": obj.get("sample_weight"),
            "sand_percent": obj.get("sand_percent"),
            "si_ug_per_g": obj.get("si_ug_per_g"),
            "silt_percent": obj.get("silt_percent"),
            "subsample_replica_weight": obj.get("subsample_replica_weight"),
            "subsample_weight": obj.get("subsample_weight"),
            "upper_depth_cm": obj.get("upper_depth_cm")
        })
        return _obj


