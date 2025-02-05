import { v4 as uuidv4 } from "uuid";
import UseDefault from "./UseDefault";

export default function CreateUuid(name) {
  UseDefault(`${name}.id`, uuidv4());
}
