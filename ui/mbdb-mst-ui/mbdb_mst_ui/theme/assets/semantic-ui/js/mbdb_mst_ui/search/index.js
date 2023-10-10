import { createSearchAppInit } from '@js/invenio_search_ui'
import {
  ActiveFiltersElement,
  BucketAggregationElement,
  BucketAggregationValuesElement,
  ErrorElement,
  SearchAppSort,
  SearchAppResultOptions,
  SearchAppSearchbarContainer,
  SearchFiltersToggleElement,
  SearchAppFacets,
  ResultCount,
} from '@js/oarepo_ui/search'
import {
  EmptyResultsElement,
  MultipleSearchBarElement,
  ResultsGridItemWithState,
  ResultsListItemWithState,
  SearchAppLayout,
} from './components'
import { parametrize, overrideStore } from 'react-overridable'

const appName = 'Mbdb_mst_ui.Search'

const SearchAppSearchbarContainerWithConfig = parametrize(SearchAppSearchbarContainer, { appName: appName })
const ResultsListItemWithConfig = parametrize(ResultsListItemWithState, { appName: appName })
const ResultsGridItemWithConfig = parametrize(ResultsGridItemWithState, { appName: appName })
const SearchAppLayoutNew = parametrize(SearchAppLayout, { appName: appName })

export const defaultComponents = {
  [`${appName}.ActiveFilters.element`]: ActiveFiltersElement,
  [`${appName}.BucketAggregation.element`]: BucketAggregationElement,
  [`${appName}.BucketAggregationValues.element`]: BucketAggregationValuesElement,
  [`${appName}.Count.element`]: ResultCount,
  [`${appName}.EmptyResults.element`]: EmptyResultsElement,
  [`${appName}.Error.element`]: ErrorElement,
  [`${appName}.ResultsGrid.item`]: ResultsGridItemWithConfig,
  [`${appName}.ResultsList.item`]: ResultsListItemWithConfig,
  [`${appName}.SearchApp.facets`]: SearchAppFacets,
  [`${appName}.SearchApp.layout`]: SearchAppLayoutNew,
  [`${appName}.SearchApp.searchbarContainer`]: SearchAppSearchbarContainerWithConfig,
  [`${appName}.SearchApp.sort`]: SearchAppSort,
  [`${appName}.SearchApp.resultOptions`]: SearchAppResultOptions,
  [`${appName}.SearchFilters.Toggle.element`]: SearchFiltersToggleElement,
  [`${appName}.SearchBar.element`]: MultipleSearchBarElement,
}

const overriddenComponents = overrideStore.getAll()

createSearchAppInit(
  { ...defaultComponents, ...overriddenComponents },
  true,
  'invenio-search-config',
  true,
)
