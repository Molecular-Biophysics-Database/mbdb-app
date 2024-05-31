import React from 'react';
import { useState } from 'react';

export default function ChooseSearchMethodDropdown() {

  const [method, setMethod] = useState('mst');

  const handleChange = (event) => {
    setMethod(event.target.value);
  };

  return (
    <>
      <form className="flex flex-col items-center justify-center my-8 mx-4 sm:flex-row" action={`${method}`} role="search">
        <div className="flex mb-2 sm:mb-0">
          <input 
            className="w-[300px] h-[50px] rounded-normal bg-dark text-primary p-4 outline-primary sm:w-[375px] lg:w-[590px]"
            type="text"
            name="q"
            placeholder="Search"
          />
          <button
            className="w-[50px] h-[50px] bg-dark rounded-normal ml-2 hover:bg-secondary transition-all sm:mx-2"
            type="submit"
            aria-label="{{ _('Search') }}"
          >
            <img className="w-5 m-auto" src="/static/images/search.png" alt="Search icon"/>
          </button>
        </div>
        <select
          className="bg-dark rounded-normal h-[50px] w-[358px] p-4 flex justify-center sm:w-[130px] lg:w-[150px] text-primary"
          value={method}
          onChange={handleChange}
        >
          <option value="mst">Only MST</option>
          <option value="bli">Only BLI</option>
          <option value="spr">Only SPR</option>
          <option value="itc">Only ITC</option>
        </select>
      </form>
    </>
  );
}