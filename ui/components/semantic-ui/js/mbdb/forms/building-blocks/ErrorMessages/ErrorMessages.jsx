import React from "react";
import PropTypes from "prop-types";
import { Label } from "mbdb-semantic-ui-react";

// One look for every block-level server/object error message, same as RIF's
// ErrorLabel: a prompting red Label with the messages joined. Returns null for
// an empty/absent list so callers can render it unconditionally.
export const ErrorMessages = ({ messages }) => {
  if (!messages || messages.length === 0) return null;
  return <Label pointing prompt content={messages.join(" ")} />;
};
ErrorMessages.propTypes = { messages: PropTypes.arrayOf(PropTypes.string) };
