from typing import Any


class ChannelIds:
  def __init__(self) -> None:
    self.channelIds = [
      "UCb_MAhL8Thb3HJ_wPkH3gcw", "UCA295QVkf9O1RQ8_-s3FVXg", "UCpFFItkfZz1qz5PpHpqzYBw",
      "UCY1kMZp36IQSyNx_9h4mpCg", "UCA19mAJURyYHbJzhfpqhpCA", "UCqnbDFdCpuN8CMEg0VuEBqA",
      "UCddiUEpeqJcYeBxX1IVBKvQ", "UCcefcZRL2oaA_uBNeo5UOWg", "UCLXo7UDZvByw2ixzpQCufnA", 
      "UCsQoiOrh7jzKmE8NBofhTnQ", "UCUyvQV2JsICeLZP4c_h40kA", "UCvjgXvBlbQiydffZU7m1_aw",
      "UCRI00CwLZdLRCWg5BdDOsNw", "UCEIwxahdLz7bap-VDs9h35A", "UC4bq21IPPbpu0Qrsl7LW0sw",
      "UCR1IuLEqb6UEA_zQ81kwXfg", "UCIlU5KDHKFSaebYviKfOidw", "UCtYKe7-XbaDjpUwcU5x0bLg",
      "UCBJycsmduvYEL83R_U4JriQ", "UCRcgy6GzDeccI7dkbbBna3Q", "UC3_BakzLfadvFrsnClMFWmQ",
      "UCmGSJVG3mCRXVOP4yZrU1Dw", "UCFN6lQpfY8XIRdhv9G-f4bg", "UConJDkGk921yT9hISzFqpzw",
      "UClWTCPVi-AU9TeCN6FkGARg", "UCyHJ94JzwY92NsBVzJ2aE3Q", "UCTqEu1wZDBju2tHkNP1dwzQ",
      "UC6nSFpj9HTCZ5t-N3Rm3-HA", "UCX6b17PVsYBQ0ip5gyeme-Q", "UCONtPx56PSebXJOxbFv-2jQ",
      "UCZYTClx2T1of7BRZ86-8fow", "UCzWQYUVCpZqtN93H8RR44Qw", "UCYbK_tjZ2OrIZFBvU6CCMiA",
      "UCxzC4EngIsMrPmbm6Nxvb-A", "UCcabW7890RKJzL968QWEykA", "UCamLstJyCa-t5gfZegxsFMw",
      "UC415bOPUcGSamy543abLmRA", "UCpMcsdZf2KkAnfmxiq2MfMQ", "UCqVEHtQoXHmUCfJ-9smpTSg",
      "UCYO_jab_esuFRV4b17AJtAw", "UCHnyfMqiRRG1u-2MsSQLbXA", "UCsXVk37bltHxD1rDPwtNM8Q",
      "UC9RM-iSvTu1uPJb8X5yp3EQ", "UCZaT_X_mc0BI-djXOlfhqWQ", "UCMiJRAwDNSNzuYeN2uWa0pA",
      "UCHpw8xwDNhU9gdohEcJu4aA", "UCK7tptUDHh-RYDsdxO1-5QQ", "UCsooa4yRKGN_zEE8iknghZA",
      "UC6n8I1UDTKP1IWjQMg6_TwA", "UC8butISFwT-Wl7EV0hUK0BQ", "UCgRQHK8Ttr1j9xCEpCAlgbQ",
      "UCEBb1b_L6zDS3xTUrIALZOw", "UCN0QBfKk0ZSytyX_16M11fA", "UCBpxspUNl1Th33XbugiHJzw",
      "UC3osNjJeuDdvyALIEP-nh0g", "UCaSCt8s_4nfkRglWCvNSDrg", "UCjgpFI5dU-D1-kh9H1muoxQ",
      "UCBa659QWEk1AI4Tg--mrJ2A", "UCdBK94H6oZT2Q7l0-b0xmMg", "UCBA9cAuPy9L5IYYXqOduIvw",
      "UCXjmz8dFzRJZrZY8eFiXNUQ", "UClZbmi9JzfnB2CEb0fG8iew", "UCUFoQUaVRt3MVFxqwPUMLCQ",
      "UCgLxmJ8xER7Y7sywMN5SfWg", "UCac1MisHGa0qtzf0oWlU8Zw", "UCSIvk78tK2TiviLQn4fSHaw",
      "UCUyvQV2JsICeLZP4c_h40kA", "UCqFzWxSCi39LnW1JKFR3efg", "UCqFzWxSCi39LnW1JKFR3efg",
      "UCccjdJEay2hpb5scz61zY6Q", "UC8CX0LD98EDXl4UYX1MDCXg", "UC6VcWc1rAoWdBCM0JxrRQ3A",
      "UCSHZKyawb77ixDdsGog4iWA", "UCVHdvAX5-R8y5l9xp6nroBQ", "UCTb6Oy0TXI03iEUdRMR9dnw",
      "UCqoAEDirJPjEUFcF2FklnBA", "UCccjdJEay2hpb5scz61zY6Q", "UCNVBYBxWj9dMHqKEl_V8HBQ",
      "UCNVBYBxWj9dMHqKEl_V8HBQ", "UCb-vZWBeWA5Q2818JmmJiqQ", "UChDKyKQ59fYz3JO2fl0Z6sg",
      "UCupvZG-5ko_eiXAupbDfxWw", "UCDrLGkZTcNCshOLiKi5NtEw", "UCWOA1ZGywLbqmigxE4Qlvuw",
      "UCrM7B7SL_g1edFOnmj-SDKg", "UCUMZ7gohGI9HcU9VNsr2FJQ", "UCF9imwPMSGz4Vq1NiTWCC7g",
      "UCjmJDM5pRKbUlVIzDYYWb6g", "UCrRttZIypNTA1Mrfwo745Sg", "UC0k238zFx-Z8xFH0sxCrPJg",
      "UCT9zcQNlyht7fRlcjmflRSA", "UC0C-w0YjGpqDXGB8IHb662A", "UCgQna2EqpzqzfBjlSmzT72w",
      "UCeLHszkByNZtPKcaVXOCOQQ", "UCjNRJBlxvvS0UXAT2Ack-QQ", "UC-J-KZfRV8c13fOCkhXdLiQ",
      "UCfM3zsQsOnfWNUppiycmBuw", "UCNjHgaLpdy1IMNK57pYiKiQ", "UCqECaJ8Gagnn7YCbPEzWH6g",
      "UCb2HGwORFBo94DmRx4oLzow", "UCi4EDAgjULwwNBHOg1aaCig", "UCDPM_n1atn2ijUwHd0NNRQw",
      "UCcgqSM4YEo5vVQpqwN-MaNw", "UCoUM-UJ7rirJYP8CQ0EIaHA", "UC0WP5P-ufpRfjbNrmOWwLBQ",
      "UCBVjMGOIkavEAhyqpxJ73Dw", "UCPHjpfnnGklkRBBTd0k6aHg", "UCmHhviensDlGQeU8Yo80zdg",
      "UC6IBMCQ6-d7p41KHxOsq4RA", "UCiMhD4jzUqG-IgPzUmmytRQ", "UCB0JSO6d5ysH2Mmqz5I9rIw",
      "UC-lHJZR3Gqxm24_Vd_AJ5Yw", "UCwx7Y3W30N8aS_tiCy2x-2g", "UCZ_cuJGBis0vi6U3bWmvDIg",
      "UCcNQQEvWA9BJG_yBQ9JkhnA", "UCf_XYgupvdx7rA44Ap3uI5w", "UCs52U_Q9TYSHtd9oxD4WN0A",
      "UConVfxXodg78Tzh5nNu85Ew", "UCNIkB2IeJ-6AmZv7bQ1oBYg", "UCcPI9kEPhyUDLBHGOhKqxOw",
      "UCVYamHliCI9rw1tHR1xbkfw", "UC-7nELDbJEPF3muAzSeT74g", "UCxqAWLTk1CmBvZFPzeZMd9A",
      "UCKWaEZ-_VweaEx1j62do_vQ", "UCFQDtftsHGzSh1-TReNT4lA", "UC6biysICWOJ-C3P4Tyeggzg",
      "UCFe-pfe0a9bDvWy74Jd7vFg", "UCUgZq9PkDp1xaEivtcfJPSg", "UC0-7PyfpOIJpNyi8WrHiyXA",
      "UCPb7xe-MQ0KiJpaKBWFZtTA", "UCycGV6fAhD_-7GPmCkkESdw", "UCG7J20LhUeLl6y_Emi7OJrA"
    ]

  def __call__(self):
    return self.channelIds