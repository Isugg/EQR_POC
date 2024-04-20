queries = [

#High alerts

{
  "bool": {
    "filter": [
      {
        "range": {
          "@timestamp": {
            "format": "strict_date_optional_time",
            "gte": "now-7d",
            "lte": "now"
          }
        }
      },
      {
        "bool": {
          "must": [],
          "filter": [
            {
              "bool": {
                "should": [
                  {
                    "term": {
                      "event.code": {
                        "value": "4649"
                      }
                    }
                  }
                ],
                "minimum_should_match": 1
              }
            }
          ],
          "should": [],
          "must_not": []
        }
      }
    ]
  }
},

{
  "bool": {
    "filter": [
      {
        "range": {
          "@timestamp": {
            "format": "strict_date_optional_time",
            "gte": "now-7d",
            "lte": "now"
          }
        }
      },
      {
        "bool": {
          "must": [],
          "filter": [
            {
              "bool": {
                "should": [
                  {
                    "term": {
                      "event.code": {
                        "value": "4719"
                      }
                    }
                  }
                ],
                "minimum_should_match": 1
              }
            }
          ],
          "should": [],
          "must_not": []
        }
      }
    ]
  }
},


#Less severe alerts

{
  "bool": {
    "filter": [
      {
        "range": {
          "@timestamp": {
            "format": "strict_date_optional_time",
            "gte": "now-7d",
            "lte": "now"
          }
        }
      },
      {
        "bool": {
          "must": [],
          "filter": [
            {
              "bool": {
                "should": [
                  {
                    "term": {
                      "event.code": {
                        "value": "4625"
                      }
                    }
                  }
                ],
                "minimum_should_match": 1
              }
            }
          ],
          "should": [],
          "must_not": []
        }
      }
    ]
  }
},

{
  "bool": {
    "filter": [
      {
        "range": {
          "@timestamp": {
            "format": "strict_date_optional_time",
            "gte": "now-7d",
            "lte": "now"
          }
        }
      },
      {
        "bool": {
          "must": [],
          "filter": [
            {
              "bool": {
                "should": [
                  {
                    "term": {
                      "event.code": {
                        "value": "4624"
                      }
                    }
                  }
                ],
                "minimum_should_match": 1
              }
            }
          ],
          "should": [],
          "must_not": []
        }
      }
    ]
  }
},

{
  "bool": {
    "filter": [
      {
        "range": {
          "@timestamp": {
            "format": "strict_date_optional_time",
            "gte": "now-7d",
            "lte": "now"
          }
        }
      },
      {
        "bool": {
          "must": [],
          "filter": [
            {
              "bool": {
                "should": [
                  {
                    "term": {
                      "event.code": {
                        "value": "4672"
                      }
                    }
                  }
                ],
                "minimum_should_match": 1
              }
            }
          ],
          "should": [],
          "must_not": []
        }
      }
    ]
  }
},

{
  "bool": {
    "filter": [
      {
        "range": {
          "@timestamp": {
            "format": "strict_date_optional_time",
            "gte": "now-7d",
            "lte": "now"
          }
        }
      },
      {
        "bool": {
          "must": [],
          "filter": [
            {
              "bool": {
                "should": [
                  {
                    "term": {
                      "event.code": {
                        "value": "4720"
                      }
                    }
                  }
                ],
                "minimum_should_match": 1
              }
            }
          ],
          "should": [],
          "must_not": []
        }
      }
    ]
  }
},

{
  "bool": {
    "filter": [
      {
        "range": {
          "@timestamp": {
            "format": "strict_date_optional_time",
            "gte": "now-7d",
            "lte": "now"
          }
        }
      },
      {
        "bool": {
          "must": [],
          "filter": [
            {
              "bool": {
                "should": [
                  {
                    "term": {
                      "event.code": {
                        "value": "4722"
                      }
                    }
                  }
                ],
                "minimum_should_match": 1
              }
            }
          ],
          "should": [],
          "must_not": []
        }
      }
    ]
  }
},

{
  "bool": {
    "filter": [
      {
        "range": {
          "@timestamp": {
            "format": "strict_date_optional_time",
            "gte": "now-7d",
            "lte": "now"
          }
        }
      },
      {
        "bool": {
          "must": [],
          "filter": [
            {
              "bool": {
                "should": [
                  {
                    "term": {
                      "event.code": {
                        "value": "4727"
                      }
                    }
                  }
                ],
                "minimum_should_match": 1
              }
            }
          ],
          "should": [],
          "must_not": []
        }
      }
    ]
  }
},

{
  "bool": {
    "filter": [
      {
        "range": {
          "@timestamp": {
            "format": "strict_date_optional_time",
            "gte": "now-7d",
            "lte": "now"
          }
        }
      },
      {
        "bool": {
          "must": [],
          "filter": [
            {
              "bool": {
                "should": [
                  {
                    "term": {
                      "event.code": {
                        "value": "4731"
                      }
                    }
                  }
                ],
                "minimum_should_match": 1
              }
            }
          ],
          "should": [],
          "must_not": []
        }
      }
    ]
  }
}
]
