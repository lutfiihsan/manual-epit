import requests
import pandas
import math

url = "https://gql.tokopedia.com/graphql/ReviewList"

headers = {
    "cookie": "_abck=9539E9647163C52A9285F6EBDFEDE322~-1~YAAQnVA7F355BeaMAQAAknmu6AvsgeKOLu0vxixr4bzIa%2FnjBRABzj8CJ2LeGipNtn4Ki6o2SGx5I3GqmrEGfnr4bI5XYpkhHjoi7AA96Fo3n0LJ4%2B8tADaXCUyv2zMRD8U91DbFHsUqvb1KB6j%2Bmd4bNRESCqDnCdupKVqOSwSy%2BYE3bSl9VGJH8THy4gzPfbK7W1Y%2FsTPqnXMcrZ20Q3gBumDcU8D%2Bdom%2F2PP1D8ZbKtHg45jUISZMUv7LxMIt2vjd%2FYo6S2eRFvuNPu5Slb3UXuFUfFOPMBXI7mQmDKYSi4Cer5XAc%2BqJbmzTBjJecG5LyCwacgqbGFhdLfV9jBrF68bIc5w1CY41ElTVkmX3%2FsM6G1G7bZ3EvkAIHvI%3D~-1~-1~-1; bm_sz=92E790D9E21565BEEE584FE9276D71ED~YAAQnVA7F395BeaMAQAAknmu6BbG0keuIe%2BLVs9PlJOqP6fxmofP672FKJISvSLzAo9SUqT%2F%2F%2Bm%2B5Q8J4uoyyZ1hBU9PnydjfPKKH2J4XqDb7DneHdwGPpB5Vm5qIfwYuA1JxUVHdUwj6oR%2FUGJ0ufntAne69WSNObeYp6nUEYbXkCEfaKOTfe%2FyA80XxNxP3wwhfas4m8qB9ktEO2MwjFaz9Nt8jcmWUHdU3DvitOMd7%2BDUzryHdijAZuQeDTMoXH3NF6kk0jTzuFkMqdPSF6AfszHubK%2Fvn4%2B8TX1xAodelrCxgMQ%3D~3622470~4274485",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "X-Version": "535e9de",
    "DNT": "1",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "content-type": "application/json",
    "accept": "*/*",
    "Referer": "https://www.tokopedia.com/bodypack/review",
    "X-Source": "tokopedia-lite",
    "X-Tkpd-Lite-Service": "zeus",
    "sec-ch-ua-platform": '"Windows"',
}
def cek_jumlah_data(shopID):
    init_query=f'[{{"operationName":"ReviewList","variables":{{"shopID":{shopID},"page":1,"limit":10,"sortBy":"create_time desc","filterBy":""}},"query":"query ReviewList($shopID: String\u0021, $limit: Int\u0021, $page: Int\u0021, $filterBy: String, $sortBy: String) {{\\n  productrevGetShopReviewReadingList(shopID: $shopID, limit: $limit, page: $page, filterBy: $filterBy, sortBy: $sortBy) {{\\n    list {{\\n      id: reviewID\\n      product {{\\n        productID\\n        productName\\n        productImageURL\\n        productPageURL\\n        productStatus\\n        isDeletedProduct\\n        productVariant {{\\n          variantID\\n          variantName\\n          __typename\\n        }}\\n        __typename\\n      }}\\n      rating\\n      reviewTime\\n      reviewText\\n      reviewerID\\n      reviewerName\\n      avatar\\n      replyText\\n      replyTime\\n      attachments {{\\n        attachmentID\\n        thumbnailURL\\n        fullsizeURL\\n        __typename\\n      }}\\n      videoAttachments {{\\n        attachmentID\\n        videoUrl\\n        __typename\\n      }}\\n      state {{\\n        isReportable\\n        isAnonymous\\n        __typename\\n      }}\\n      likeDislike {{\\n        totalLike\\n        likeStatus\\n        __typename\\n      }}\\n      badRatingReasonFmt\\n      __typename\\n    }}\\n    hasNext\\n    shopName\\n    totalReviews\\n    __typename\\n  }}\\n}}\\n"}}]'

    response = requests.post(url, headers=header, data=init_query)

    jumlah_data = response.json()[0]['data']['productrevGetShopReviewReadingList']['totalReviews']
    jumlah_page = math.ceil(jumlah_data/60) + 1

    return jumlah_data, jumlah_page

def scrape_tokeped(shopID):
    print("Mulai scrape data ke tokopedia....")
    jml_data, jml_page = cek_jumlah_data("6504579")
    hasil = []
    for page, data in zip(range(1, jml_page), range(0, jml_data, 10)):
        query = f'[{{"operationName":"ReviewList","variables":{{"shopID":{shopID},"page":{page},"limit":10,"sortBy":"create_time desc","filterBy":""}},"query":"query ReviewList($shopID: String\u0021, $limit: Int\u0021, $page: Int\u0021, $filterBy: String, $sortBy: String) {{\\n  productrevGetShopReviewReadingList(shopID: $shopID, limit: $limit, page: $page, filterBy: $filterBy, sortBy: $sortBy) {{\\n    list {{\\n      id: reviewID\\n      product {{\\n        productID\\n        productName\\n        productImageURL\\n        productPageURL\\n        productStatus\\n        isDeletedProduct\\n        productVariant {{\\n          variantID\\n          variantName\\n          __typename\\n        }}\\n        __typename\\n      }}\\n      rating\\n      reviewTime\\n      reviewText\\n      reviewerID\\n      reviewerName\\n      avatar\\n      replyText\\n      replyTime\\n      attachments {{\\n        attachmentID\\n        thumbnailURL\\n        fullsizeURL\\n        __typename\\n      }}\\n      videoAttachments {{\\n        attachmentID\\n        videoUrl\\n        __typename\\n      }}\\n      state {{\\n        isReportable\\n        isAnonymous\\n        __typename\\n      }}\\n      likeDislike {{\\n        totalLike\\n        likeStatus\\n        __typename\\n      }}\\n      badRatingReasonFmt\\n      __typename\\n    }}\\n    hasNext\\n    shopName\\n    totalReviews\\n    __typename\\n  }}\\n}}\\n"}}]'
        response = requests.post(url, headers=header, data=query)
        products = response.json()[0]['data']['productrevGetShopReviewReadingList']['list']['product']
        hasil.extend(products)

    dtFrame = pd.DataFrame.from_dict(hasil)
    dtFrame.to_csv('data_tokped_2.csv', encoding='utf-8')
    print("Selesai ...")

shopID = "6504579"
scrape_tokeped(shopID)