import "../../less/mbdb/components.less";

import { overrideStore } from "react-overridable";
import { RequestCommentInput } from "./components/RequestCommentInput";

overrideStore.add("RequestCommentInput", RequestCommentInput);
