import React from "react";
import { MultipleOptionsSearchBarRSK } from "@js/invenio_search_ui/components";

export const MultipleSearchBarElement = ({ queryString, onInputChange }) => {
  // TODO: no search bar element in the header, so this should not be used
  // const headerSearchbar = document.getElementById("header-search-bar");
  // const searchbarOptions = JSON.parse(headerSearchbar.dataset.options);

  return (
      <input type="text" value={queryString} onChange={onInputChange} placeholder="Search..."/>
    // <MultipleOptionsSearchBarRSK
    //   // options={searchbarOptions}
    //   onInputChange={onInputChange}
    //   queryString={queryString}
    //   placeholder="Search..."
    // />
  );
};
