import React from "react";
import CustomField from "../../buildingBlocks/CustomField";

function Ph( { name } ) {

    return(
        <>
            <div className="bg-white p-3 rounded-lg text-dark flex">
                <div className="m-auto font-bold mr-10">
                    pH
                </div>
                <div>
                    <CustomField
                        name={name}
                        label='Value'
                        type='number'
                        tooltip='The pH value of the chemical environment'
                        width='w-[8.5rem]'
                    />
                </div>
            </div>
        </>
    )

}

export default Ph;