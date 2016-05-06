class ProductType:
    School = "School"
    Home = "Home"

class Partners:
    COOL = "Cool"
    MINI = "Mini"
    INDO = "Indo"
    Rupe = "Rupe"
    CEHK = "Cehk"
    ECSP = "Ecsp"


class LevelInfoCool:
    LEVEL_0A = "0A"
    LEVEL_0B = "0A"
    LEVEL_1 = "1"
    LEVEL_2 = "2"
    LEVEL_3 = "3"
    LEVEL_4 = "4"
    LEVEL_5 = "5"
    LEVEL_6 = "6"
    LEVEL_7 = "7"
    LEVEL_8 = "8"
    LEVEL_9 = "9"
    LEVEL_10 = "10"
    LEVEL_11 = "11"
    LEVEL_12 = "12"
    LEVEL_13 = "13"
    LEVEL_14 = "14"


class LevelInfoMini:
    LEVEL_1 = "1"
    LEVEL_2 = "2"
    LEVEL_3 = "3"
    LEVEL_4 = "4"
    LEVEL_5 = "5"
    LEVEL_6 = "6"
    LEVEL_7 = "7"
    LEVEL_8 = "8"
    LEVEL_9 = "9"
    LEVEL_10 = "10"
    LEVEL_11 = "11"
    LEVEL_12 = "12"
    LEVEL_13 = "13"
    LEVEL_14 = "14"
    LEVEL_15 = "15"
    LEVEL_16 = "16"

account_info = [
    {
        "tags" : {
            "partner": Partners.COOL,
            "Product Type": ProductType.School,
        },
        "mainRedemptionCode": "S15SCHOOLMAIN",
        "freeRedemptionCode": "S15SCHOOLF1D",
        "divisionCode": "SSCNSH2",
        "productId": "63",
    },
    {
        "tags" : {
            "partner": Partners.COOL,
            "Product Type": ProductType.Home,
        },
        "mainRedemptionCode": "S15HOMEPL20MAIN",
        "freeRedemptionCode": "S15HOMEPL20F1D",
        "divisionCode": "SSCNSH2",
        "productId": "64",
    },
    {
        "tags" : {
            "partner": Partners.MINI,
            "Product Type": ProductType.School,
        },
        "mainRedemptionCode": "S15SCHOOLMAIN",
        "freeRedemptionCode": "S15SCHOOLF1D",
        "divisionCode": "CNMNNJ3",
        "productId": "65",
    },
    {
        "tags" : {
            "partner": Partners.MINI,
            "Product Type": ProductType.Home,
        },
        "mainRedemptionCode": "S15HOMEPL20MAIN",
        "freeRedemptionCode": "S15HOMEPL20F1D",
        "divisionCode": "CNMNNJ3",
        "productId": "66",
    }
]
