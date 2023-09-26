import React from "react";
import { MinimalInputForm, initForm } from "@mbdb/input-form/lib";
import { getKeeper } from "@mbdb/input-form/lib/context/keeper";
import { Config } from "@mbdb/input-form/lib/config";
import { FormContext } from "@mbdb/input-form/lib/context";
import { FormContextHandler } from "@mbdb/input-form/lib/context/handler";
import { Mbdb } from "@mbdb/input-form/lib/mbdb";
import { submitToMbdb } from "@mbdb/input-form/lib/mbdb/submit";
import { Data } from "@mbdb/input-form/lib/schema/data";
import { Persistence } from "@mbdb/input-form/lib/schema/persistence";
import { Uuid } from "@mbdb/input-form/lib/schema/uuid";
import { ErrorDialog } from "@mbdb/input-form/lib/ui/error-dialog";
import { LoadFileButton } from "@mbdb/input-form/lib/ui/load-file-button";
import { doDownload, FileTypes } from "@mbdb/input-form/lib/util/download";
import { Button, Icon } from "semantic-ui-react";

const MstSchemaName = "mst";

function makeBaseUrl() {
    return window.location.protocol + "//" + window.location.host;
}

function makeMbdbErrors(errors) {
    const out = [];

    for (const err of errors) {
        const field = err.field;
        const msgs = err.messages;

        if (field && msgs && Array.isArray(msgs)) {
            out.push(`${field}: ${msgs.join(', ')}`);
        }
    }

    return out;
}

function makeSubmissionErrorContent(code, text, errors) {
    return (
        code !== 0
            ? (
                <>
                    <div className='mbdbi-deposition-error-report mbdbi-center-text mbdbi-strong'>
                        Deposition failed because the database reported an error
                    </div>
                    <div className='mbdbi-deposition-error-report' style={{ display: 'grid', gridTemplateColumns: 'auto 1fr', gap: 'var(--mbdbi-2hgap)' }}>
                        <div>Status code</div><div>{code}</div>
                        <div>Message</div><div>{text}</div>
                        <div>Errors</div><div>{errors.map((err, idx) => <div key={idx}>{err}</div>)}</div>
                    </div>
                </>
            ) : (
                <>
                    <div className='mbdbi-deposition-error-report mbdbi-center-text mbdbi-strong'>
                        Deposition failed because the remote server could not have been contacted
                    </div>
                    <div className='mbdbi-deposition-error-report mbdbi-center-text'>
                        {text}
                    </div>
                </>
            )
    );
}

function makeSubmissionErrorDialog(code, text, errors) {
    return {
        title: 'Cannot deposit record because there was an issue on the backend',
        icons: [<Icon name='warning' />, <Icon name='database' />],
        content: makeSubmissionErrorContent(
            code,
            text,
            errors
        ),
    };
}

function showFormHasErrorsDialog(errors) {
    ErrorDialog.show({
        title: 'Cannot deposit record',
        icons: [<Icon name='warning' />, <Icon name='clipboard list' />],
        content: (
            <>
                <div className='mbdbi-deposition-error-report mbdbi-center-text mbdbi-strong'>Cannot deposit record because there are some invalid items in the form.</div>
                <ul className='mbdbi-deposition-error-report'>
                    {errors.map((err, idx) => (
                        <li className='mbdbi-deposition-error-report' key={idx}>
                            <div>{Data.Path.toString(err.path)}</div>
                            <div>{err.message}</div>
                        </li>
                    )) ?? null}
                </ul>
            </>
        )
    });
}

async function createDraft(apiEndpoint, data) {
    const baseUrl = makeBaseUrl();

    const { toApi, errors } = Mbdb.toData(data);
    if (errors.length > 0) {
        showFormHasErrorsDialog(errors);
        return;
    }

    try {
        const resp = await submitToMbdb(baseUrl, apiEndpoint, toApi);
        if (!resp.ok) {
            resp.json().then((j) => {
                ErrorDialog.show(makeSubmissionErrorDialog(resp.status, j.message || resp.statusText, makeMbdbErrors(j.errors ?? [])));
            }).catch(() => {
                ErrorDialog.show(makeSubmissionErrorDialog(resp.status, resp.statusText, []));
            });

            return;
        }
    } catch (e) {
        ErrorDialog.show(makeSubmissionErrorDialog(0, e.message, []));
    }
}

function ControlsTape({ ctxHandler, createDraftUrl, dataId }) {
    const getData = () => getKeeper().get(dataId).data;

    return (
        <div className="mbdbv-input-controls-tape">
            <div>
                <LoadFileButton
                    title="Load from JSON"
                    onLoaded={(file) => {
                        Persistence.fromFile(file).then((json) => {
                            try {
                                FormContext.load(json, getData());
                                ctxHandler.update();
                            } catch (e) {
                                ErrorDialog.show({ title: 'Cannot load form from Internal Input file', content: <div>{e.message}</div> });
                            }
                        }).catch((e) => {
                            ErrorDialog.show({ title: 'Cannot load form from Internal Input file', content: <div>{e.message}</div> });
                        });
                    }}
                    color="teal"
                    fluid
                />
            </div>

            <div>
                <Button
                    onClick={() => {
                        const json = Persistence.toJson(getData().data, false);
                        doDownload("mst_ui_input", json, FileTypes.json);
                    }}
                    color="teal"
                    fluid
                >
                    <Icon name="download" />
                    Save to JSON
                </Button>
            </div>

            <div />

            <div>
                <Button
                    onClick={() => createDraft(createDraftUrl, getKeeper().get(dataId).data)}
                    color="blue"
                    fluid
                >
                    <Icon name="angle double right" />
                    <span style={{ display: 'inline-block', width: 'var(--mbdbi-2hgap)' }} />
                    Create draft
                </Button>
            </div>
        </div>
    );
}

export function DepositForm({ createDraftUrl }) {
    const dataId = React.useMemo(() => Uuid.get(), []);
    const { ctxHandler } = React.useMemo(() => {
        const keeper = getKeeper();
        initForm(dataId, MstSchemaName);

        const ctxGetter = () => keeper.get(dataId).data;
        const ctxUpdater = (handler) => setContextValue({ handler });
        const ctxHandler = FormContextHandler.make(ctxGetter, ctxUpdater);

        return { ctxHandler };
    }, []);
    const [_contextValue, setContextValue] = React.useState({ handler: ctxHandler });

    React.useEffect(() => {
        Config.set({
            vocabulariesApiEndpoint: 'vocabularies',
        });
    }, []);

    return (
        <div className="mbdbv-input-root">
            <ControlsTape ctxHandler={ctxHandler} createDraftUrl={createDraftUrl} dataId={dataId} />
            <MinimalInputForm dataId={dataId} schemaName={MstSchemaName} formContextHandler={ctxHandler} />
        </div>
    );
};
