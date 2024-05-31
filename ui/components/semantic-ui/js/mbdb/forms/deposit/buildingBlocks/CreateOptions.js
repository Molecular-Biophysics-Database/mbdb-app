function CreateOptions(list, label) {
    if (list && list.some(item => item.name !== undefined)) {
        return list.map(item => ({ value: item.name, label: item.name }));
    } else {
        return [{ label }];
    }
}

export default CreateOptions;