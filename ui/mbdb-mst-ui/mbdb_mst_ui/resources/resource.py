from oarepo_ui.resources.resource import RecordsUIResource

from flask import g, request
from flask_resources import (
    resource_requestctx,
)
from invenio_records_resources.resources.records.resource import (
    request_read_args,
    request_view_args,
)

from oarepo_ui.resources.catalog import get_jinja_template
from oarepo_ui.proxies import current_oarepo_ui


class MbdbMstUIResource(RecordsUIResource):
    pass


    @request_read_args
    @request_view_args
    def detail(self):
        """Returns item detail page."""
        """Returns item detail page."""
        record = self._get_record(resource_requestctx, allow_draft=True)
        # TODO: handle permissions UI way - better response than generic error
        serialized_record = self.config.ui_serializer.dump_obj(record.to_dict())
        # make links absolute
        if "links" in serialized_record:
            for k, v in list(serialized_record["links"].items()):
                if not isinstance(v, str):
                    continue
                if not v.startswith("/") and not v.startswith("https://"):
                    v = f"/api{self.api_service.config.url_prefix}{v}"
                    serialized_record["links"][k] = v

        export_path = request.path.split("?")[0]
        if not export_path.endswith("/"):
            export_path += "/"
        export_path += "export"

        layout = current_oarepo_ui.get_layout(self.get_layout_name())
        _catalog = current_oarepo_ui.catalog

        template_def = self.get_template_def("detail")
        source = get_jinja_template(_catalog, template_def)

        extra_context = dict()
        ui_links = self.expand_detail_links(identity=g.identity, record=record)

        serialized_record["extra_links"] = {
            "ui_links": ui_links,
            "export_path": export_path,
            "search_link": self.config.url_prefix,
        }

        self.run_components(
            "before_ui_detail",
            resource=self,
            record=serialized_record,
            identity=g.identity,
            extra_context=extra_context,
            args=resource_requestctx.args,
            view_args=resource_requestctx.view_args,
            ui_links=ui_links,
            ui_config=self.config,
            ui_resource=self,
            layout=layout,
            component_key="search",
        )

        metadata = dict(serialized_record.get("metadata", serialized_record))
        return _catalog.render(
            "detail",
            __source=source,
            metadata=metadata,
            ui=dict(serialized_record.get("ui", serialized_record)),
            layout=dict(layout),
            record=serialized_record,
            extra_context=extra_context,
        )
