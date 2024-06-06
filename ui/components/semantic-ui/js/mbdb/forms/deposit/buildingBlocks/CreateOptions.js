function CreateOptions(list, label) {
    if (list && list.some(item => item.name !== undefined && item.id !== undefined)) {
        return list.map(item => {
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

export default CreateOptions;