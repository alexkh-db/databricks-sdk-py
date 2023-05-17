import base64
import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

created = w.global_init_scripts.create(name=f'sdk-{time.time_ns()}',
                                       script=base64.b64encode(("echo 1").encode()).decode(),
                                       enabled=True,
                                       position=10)

by_id = w.global_init_scripts.get(get=created.script_id)

# cleanup
w.global_init_scripts.delete(delete=created.script_id)