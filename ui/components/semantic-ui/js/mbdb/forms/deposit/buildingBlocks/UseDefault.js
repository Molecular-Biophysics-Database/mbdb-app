import { getIn, useFormikContext } from "formik";
import { useEffect } from "react";

function UseDefault(name, content) {

    const { setFieldValue, values } = useFormikContext();

    useEffect(() => {
        const existingValue = getIn(values, name);
        if (existingValue === undefined) {
            setFieldValue(name, content)
        }
    }, [content, name, setFieldValue, values])
}

export default UseDefault;