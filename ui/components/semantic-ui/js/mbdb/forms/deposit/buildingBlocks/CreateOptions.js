function CreateOptions(list, label) {
    if (list && list.some(item => item.name !== undefined || item.id !== undefined)) {
        if (list.some(item => item.name === undefined)) {
            return [{ label }];
        }
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