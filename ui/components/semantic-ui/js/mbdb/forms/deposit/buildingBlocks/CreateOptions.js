export default function CreateOptions(list, label) {
  if (
    list &&
    list.length >= 1 &&
    list.some(
      (item) =>
        item.name !== undefined || item.name !== "" || item.id !== undefined
    )
  ) {
    const filteredList = list.filter((item) => item?.name !== undefined);

    if (filteredList.length === 0) {
      return [{ label }];
    }

    return filteredList.map((item) => {
      return {
        id: item.id,
        value: item.name,
        label: item.name,
      };
    });
  } else {
    return [{ label }];
  }
}
