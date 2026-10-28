# USA turu analüüsi tugisüsteem: õppedemo

Andmeallikas: SIMULEERITUD; ei ole ajalooline USA turuandmestik

## Tootlus ja risk

```text
                             kogutootlus    CAGR  volatiilsus  max_langus
AKTSIA_A_SIM                     -0.1493 -0.0525       0.2038     -0.3174
AKTSIA_B_SIM                     -0.2844 -0.1055       0.2228     -0.3966
VOLAKIRI_SIM                     -0.0986 -0.0340       0.0562     -0.1433
osta_hoia_vordsed_algkaalud      -0.1774 -0.0630       0.1313     -0.2648
```

Portfell: võrdsed algkaalud, osta-ja-hoia, kuludeta; kaalud triivivad. Võrdlusvara on CSV esimene veerg.

## Mudelid

```text
       mudel  CV_RMSE  test_RMSE
        null 0.012650   0.014569
       Ridge 0.012728   0.014594
RandomForest 0.012809   0.014855
```

Ajapiirid: {"treening_lopp": "2024-04-30 00:00:00", "test_algus": "2024-05-02 00:00:00", "test_ridu": 148}

## SMA strateegia

```json
{
  "kogutootlus": -0.1857780774522655,
  "CAGR": -0.0662134866759514,
  "volatiilsus": 0.12202636470500522,
  "max_langus": -0.2497100696583171
}
```

Tehingukulu 0,1% ühes suunas; signaal t sulgemise järel, täitmine t+1 sulgemisel. Raha intress 0.

Madal prognoosiviga ei tõenda kasumlikku strateegiat. Fundamentaal- ja dokumendiuuring on eraldi praktikumid; raport ei sisalda automaatset ostusoovitust.
