import React from "react";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import ValueUnit from "@mbdb_deposit/buildingBlocks/ValueUnit";

export default function PrimaryLaserWavelength({ name }) {
    const unitOptions = [
        { value: "Å", label: "Å" },
        { value: "nm", label: "nm" },
        { value: "μm", label: "μm" },
        { value: "mm", label: "mm" },
        { value: "cm", label: "cm" },
        { value: "m", label: "m" },
    ];
    return (
        <FormWrapper headline="Primary laser wavelenght">
            <ValueUnit
                options={unitOptions}
                name={name}
                tooltipValue="Numerical value of the wavelength"
                tooltipUnit="The unit of the wavelength"
            />
        </FormWrapper>
    )
}
