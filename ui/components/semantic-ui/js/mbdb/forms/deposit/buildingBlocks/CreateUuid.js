import { v4 as uuidv4 } from 'uuid';
import UseDefault from './UseDefault';

function CreateUuid(name) {
    UseDefault(`${name}.id`, uuidv4());
}

export default CreateUuid;