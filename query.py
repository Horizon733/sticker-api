search_query = """
query SearchStickerSample {
  sticker {
    searchStickers(
      req:{
        searchStickersParams:{searchText: "search_text", numberResults: number_results},
        stickerUserContext:{countryCode: US, localTimeZoneUTCOffsetMinutes: 2,locale: EN_US}
      }){
      stickerResults {
        items {
          itemType
          id
          pngURL
          thumbnailURL
        }
      }
    }
  }
}
"""

trending_query = """
query SearchStickerSample {
  sticker {
    trendingStickers(
      req:{
        numberResults: number_results,
        stickerUserContext:{countryCode: US, localTimeZoneUTCOffsetMinutes: 2,locale: EN_US}
      }) {
      stickerResults{
        items {
          id
          pngURL
          thumbnailURL
        }
      }
    }
  }
}
"""

category_query = """
query SearchStickerSample{
  sticker {
    categoryStickers(
      req:{
        numberCategories: number_category,
        numberResults: number_results,
        stickerUserContext:{countryCode: US, localTimeZoneUTCOffsetMinutes: 2,locale: EN_US}
      }) {
      stickerSection {
        stickerCategories {
          category
          stickerResults {
            items {
              itemType
              id
              pngURL
              thumbnailURL
            }
          }
        }
      }
    }
  }
}
"""