import { createSearchAppsInit } from '@js/oarepo_ui'
import {
  EmptyResultsElement,
  MultipleSearchBarElement,
  ResultsGridItemWithState,
  SearchAppLayout,
} from './components'
import {SearchAppSearchbarContainer, parseSearchAppConfigs} from '@js/oarepo_ui'
import { parametrize, overrideStore } from 'react-overridable'

const [{overridableIdPrefix}, ...otherSearchAppConfigs] = parseSearchAppConfigs()

const SearchAppSearchbarContainerWithConfig = parametrize(SearchAppSearchbarContainer, { appName: overridableIdPrefix })
const ResultsGridItemWithConfig = parametrize(ResultsGridItemWithState, { appName: overridableIdPrefix })

export const componentOverrides = {
  [`${overridableIdPrefix}.EmptyResults.element`]: EmptyResultsElement,
  [`${overridableIdPrefix}.ResultsGrid.item`]: ResultsGridItemWithConfig,
  [`${overridableIdPrefix}.SearchApp.searchbarContainer`]: SearchAppSearchbarContainerWithConfig,
  [`${overridableIdPrefix}.SearchBar.element`]: MultipleSearchBarElement,
}

createSearchAppsInit(
    {componentOverrides}
)
