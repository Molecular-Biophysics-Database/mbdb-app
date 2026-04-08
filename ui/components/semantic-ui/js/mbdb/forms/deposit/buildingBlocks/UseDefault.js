import { getIn, useFormikContext } from "formik";
import { useEffect } from "react";

export default function UseDefault(name, content) {
  const { setFieldValue, values } = useFormikContext();

  useEffect(() => {
    const existingValue = getIn(values, name);
    
    const shouldSetDefault =
      existingValue === undefined ||
      existingValue === null ||
      (Array.isArray(existingValue) && existingValue.length === 0);

    if (shouldSetDefault) {
      setFieldValue(name, content);
    }
  }, [content, name, setFieldValue, values]);
}
